- install python 3.9.11
- install libraries from requirements.txt: pip install -r requirements.txt
    If there an error. Try install deepface library without dependencies: pip install --no-deps deepface
- load your face to folder /users
- run program: python securix.py
    a) If you want to work with video
        in line 9:
            camera = cv2.VideoCapture("foot.mp4")
        change "foot.mp4" to your file path
    b) If you want to work with webcamera
        in line 9:
            camera = cv2.VideoCapture(0)