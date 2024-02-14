import cv2
from deepface import DeepFace


def face_capture():
    clf = cv2.CascadeClassifier(r"filter/haarcascade_frontalface_default.xml")
    clfp = cv2.CascadeClassifier(r"filter/haarcascade_profileface.xml")
    clf_alt = cv2.CascadeClassifier(r"filter/haarcascade_frontalface_alt_tree.xml")
    clb = cv2.CascadeClassifier(r"filter/haarcascade_fullbody.xml")
    camera = cv2.VideoCapture("video/toni_video.mp4")

    while True:
        ret, frame = camera.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(gray,1.2,3)
        faces_alt = clf_alt.detectMultiScale(gray,1.1,5)
        faces_profile = clfp.detectMultiScale(gray,1.1,5)
        bodies = clb.detectMultiScale(gray,1.1,5)
        
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 1)
            face_recogn(frame)
        for (x, y, width, height) in faces_profile:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 200, 255), 1)
        for (x, y, width, height) in faces_alt:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 1)
        for (x, y, w, h) in bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow('Securix', frame)
        if cv2.waitKey(1) == ord('q'):#press q key to quit
            break
    camera.release()
    cv2.destroyAllWindows()

def face_recogn(frame):#face check
    result = DeepFace.find(frame, db_path="users")
    if result:
        print("Known person")
    else:
        print("Unknown person")

    

def main():
    face_capture()

if __name__ == "__main__":
    main()
