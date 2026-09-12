<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# [FrameMatch da] 🎯


## Basic Details
### Team Name: [Error 404]


### Team Members
- Team Lead: [Gayathri Sunil] - [College of engineering attingal]
- Member 2: [Asna Sajeer] - [College of engineering attingal]



### Project Description
[This project is an AI-based humorous reaction system using facial emotion recognition.
It detects whether a user is feeling sad or happy.
Based on the emotion and selected situation, it recommends a suitable Malayalam movie clip.
The dataset contains clips categorized into breakup, food love, sad, motor, and comedy.
The goal is to create an interactive, entertaining experience using AI and computer vision.]


### The Problem (that doesn't exist)
[People often struggle to find the perfect funny reaction for their mood or situation .Existing emotion detection systems are too seriopus,so there is a need for a fun way to turn emotions into relatable malayalam movie reactions.]

### The Solution (that nobody asked for)
[FrameMatch da uses facial emotion recoginition to detect whether a user is sad or happy and matches it with a selected situation such as breakup,foodlove,sad,motor or comedy.It then recommends suitable reaction clip,turning everyday emotions into entertaining cinematc moments.]

## Technical Details
### Technologies/Components Used
For Software:
- [Python]
- [OpenCV]
- [Deep]
- [Pandas,CSV Dataset,MoviePy/VLC,VS code]


For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# [FrameMatch da] 🎯


## Basic Details
### Team Name: [Error 404]


### Team Members
- Team Lead: [Gayathri Sunil] - [College of engineering attingal]
- Member 2: [Asna Sajeer] - [College of engineering attingal]



### Project Description
[This project is an AI-based humorous reaction system using facial emotion recognition.
It detects whether a user is feeling sad or happy.
Based on the emotion and selected situation, it recommends a suitable Malayalam movie clip.
The dataset contains clips categorized into breakup, food love, sad, motor, and comedy.
The goal is to create an interactive, entertaining experience using AI and computer vision.]


### The Problem (that doesn't exist)
[People often struggle to find the perfect funny reaction for their mood or situation .Existing emotion detection systems are too seriopus,so there is a need for a fun way to turn emotions into relatable malayalam movie reactions.]

### The Solution (that nobody asked for)
[FrameMatch da uses facial emotion recoginition to detect whether a user is sad or happy and matches it with a selected situation such as breakup,foodlove,sad,motor or comedy.It then recommends suitable reaction clip,turning everyday emotions into entertaining cinematc moments.]

## Technical Details
### Technologies/Components Used
For Software:
- [Python]
- [OpenCV]
- [Deep]
- [Pandas,CSV Dataset,MoviePy/VLC,VS code]


For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:
# Installation
[commands]

# Run
[commands]

### Project Documentation
For Software:

# Screenshots (Add at least 3)
![c:\Users\lenovo\Documents\redme1.jpeg](FrameMatch-Scene Selection and Mood Detection Interface)
This screenshot shows the main interface of the FrameMatch application. Users can upload a reaction image and select a relevant situation, such as comedy, breakup, food love, sad, or motor. By clicking “OK - Detect mood,” the system analyzes the user's facial expression and identifies a movie scene based on the detected mood and selected situation.

![c:\Users\lenovo\Documents\redme2.jpeg](Uploaded image and initial mood classification)
This screenshot shows the FrameMatch application after a user uploads an image named “PARU PIC.jpeg” and selects the “comedy” situation. The uploaded image is displayed with a preview, and the “OK - Detect mood” button is available to initiate analysis. The result panel indicates that the image has been classified as “Unknown”, after which the system proceeds to search for the best matching movie scene. This demonstrates the image-upload, situation-selection, and initial mood-classification stages of the application6

![c:\Users\lenovo\Documents\redme3.jpeg](FrameMatch-Generated Meme Based on the Uploaded Image)
This screenshot shows the final output of the FrameMatch application, where a funny meme is generated based on the user's uploaded image and the selected situation. The system uses the detected mood and matching movie-scene content to produce a humorous result, demonstrating the meme-generation stage of the application.

# Diagrams
![Workflow](┌──────────────────────────────┐
│          USER                │
│  Facial Expression +         │
│  Situation Selection         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       INPUT MODULE           │
│  Webcam / User Interface     │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   FACIAL EMOTION MODULE      │
│  OpenCV + DeepFace           │
│  Detects: Sad / Happy        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│    CLIP SELECTION MODULE     │◄──────────────┐
│  Emotion + Situation Match   │               │
└──────────────┬───────────────┘               │
               │                               │
               ▼                               │
┌──────────────────────────────┐      ┌─────────┴────────────────────┐
│       DATASET MODULE         │      │       CSV DATABASE           │
│  Pandas                      │◄─────┤  Clip ID                     │
│  Filters matching clips      │      │  Emotion                     │
└──────────────┬───────────────┘      │  Situation                   │
               │                      │  Roast Level                  │
               ▼                      │  Clip Path                    │
┌──────────────────────────────┐      └───────────────────────────────┘
│      VIDEO OUTPUT MODULE     │
│  VLC / MoviePy               │
│  Plays Selected Clip         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│       USER INTERFACE         │
│  Display / Play Reaction     │
└──────────────────────────────┘)
*The system captures the user’s facial expression through a webcam, detects the emotion as sad or happy using DeepFace, and combines it with the selected situation. The system then searches the CSV dataset for a matching Malayalam movie clip and plays the most suitable reaction video

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[https://drive.google.com/file/d/1LZqXh8tEUYLLgX1zb5pkMIlA_5DhskQ9/view?usp=drive_link]
The video demonstrates the working of an emotion-based Malayalam movie clip recommendation system. First, the application uses the webcam to capture the user's facial expression. The facial emotion is analyzed and classified into one of two categories: sad or happy. Based on the user's emotion and the selected situation, such as breakup, food love, sad, motor, or comedy, the system searches the available clip dataset.

The dataset contains information about each movie clip, including its clip ID, emotion, situation, roast level, and video path. The system identifies the most suitable clip by matching the detected emotion and selected situation. Finally, the selected Malayalam movie clip is played as a personalized reaction. The demonstration shows how facial emotion recognition, dataset filtering, and video selection work together to create an interactive and entertaining user experience.

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
- [Gayathri Sunil]: [frontend]
- [Asna Sajeer]: [backend]
-

---
