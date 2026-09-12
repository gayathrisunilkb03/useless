def run_test():
    print('Testing imports...')
    try:
        from flask import Flask
        print('Flask import: OK')
    except Exception as e:
        print('Flask import: FAILED -', e)

    try:
        from deepface import DeepFace
        print('DeepFace import: OK')
    except Exception as e:
        print('DeepFace import: FAILED -', e)

if __name__ == '__main__':
    run_test()
