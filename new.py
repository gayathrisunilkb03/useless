from flask import Flask, request, render_template, redirect, url_for, send_file
import os
import csv
import uuid
import numpy as np

try:
    import cv2
except Exception:
    cv2 = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIE_CSV = os.path.join(BASE_DIR, 'movie.csv')

app = Flask(__name__, static_folder='')  # serve project root for demo clips

SITUATIONS = ['comedy', 'motor', 'sad', 'breakup', 'food love', 'thall']


def detect_emotion(image_path):
    """Use `FER` library for emotion detection if available, otherwise
    fall back to the existing OpenCV heuristic.
    """
    try:
        from fer import FER
        # load image (FER expects RGB image in numpy array form)
        if cv2 is not None:
            img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
            if img is None:
                return 'unknown'
        else:
            from PIL import Image
            img = np.array(Image.open(image_path).convert('RGB'))

        detector = FER(mtcnn=True)
        faces = detector.detect_emotions(img)
        if faces:
            # choose the largest face by area
            face = max(faces, key=lambda f: f['box'][2] * f['box'][3])
            emotions = face.get('emotions', {})
            if emotions:
                dominant = max(emotions, key=lambda k: emotions[k])
                mapping = {
                    'happy': 'happy',
                    'sad': 'sad',
                    'angry': 'angry',
                    'surprise': 'surprised',
                    'fear': 'scared',
                    'disgust': 'disgusted',
                    'neutral': 'neutral'
                }
                return mapping.get(dominant, dominant or 'unknown')
        # no faces or no confident result
        return opencv_detect_emotion(image_path)
    except Exception:
        try:
            return opencv_detect_emotion(image_path)
        except Exception:
            return 'unknown'


def opencv_detect_emotion(image_path: str) -> str:
    """Very small heuristic-based detector using OpenCV Haar cascades.

    - detects smile -> 'happy'
    - if face found but no smile -> 'neutral'
    - if no face -> 'unknown'
    This is a fallback for local testing only; accuracy is limited.
    """
    if cv2 is None:
        return 'unknown'
    img = cv2.imread(image_path)
    if img is None:
        return 'unknown'
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
    if len(faces) == 0:
        return 'unknown'
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
        if len(smiles) > 0:
            return 'happy'
        # simple texture heuristic to guess surprise
        if np.std(roi_gray) > 60:
            return 'surprised'
        return 'neutral'


def load_clips():
    clips = []
    if not os.path.exists(MOVIE_CSV):
        return clips
    with open(MOVIE_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            # normalize fields
            r['roast_level'] = int(r.get('roast_level') or 0)
            clips.append(r)
    return clips


@app.route('/', methods=['GET'])
def index():
    clips = load_clips()
    return render_template('index.html', situations=SITUATIONS, results=None)


@app.route('/audio/<path:filename>')
def audio(filename):
    audio_path = os.path.join(BASE_DIR, filename)
    if not os.path.isfile(audio_path):
        return '', 404
    return send_file(audio_path, mimetype='audio/mp4', conditional=True)


@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files.get('image')
    situation = request.form.get('situation')
    if not file:
        return redirect(url_for('index'))

    uploads = os.path.join(BASE_DIR, 'uploads')
    os.makedirs(uploads, exist_ok=True)
    filename = f"{uuid.uuid4().hex}_{file.filename}"
    path = os.path.join(uploads, filename)
    file.save(path)

    detected = detect_emotion(path)

    clips = load_clips()
    # filter by detected emotion and/or situation
    filtered = []
    for c in clips:
        match_emotion = (detected != 'unknown' and c['emotion'].lower() == detected.lower())
        match_situation = (situation and c['situation'] == situation)
        if match_emotion or match_situation:
            filtered.append(c)

    # fallback: if nothing matched, show top roast clips
    if not filtered:
        filtered = sorted(clips, key=lambda x: -x['roast_level'])[:6]
    else:
        filtered = sorted(filtered, key=lambda x: -x['roast_level'])

    return render_template('index.html', situations=SITUATIONS, results=filtered, detected=detected, uploaded=path)


if __name__ == '__main__':
    app.run(debug=True)
