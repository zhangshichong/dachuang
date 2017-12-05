import cv2
import time

print('Press esc to exit')
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imgWindow = cv2.namedWindow('face_detection', cv2.WINDOW_NORMAL)

def detect_face():
    cap = cv2.VideoCapture(1)
    next_cap_time = time.time()
    faces = []
    if not cap.isOpened(): print('cannot open camera')
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        if next_cap_time < time.time():
            next_cap_time = time.time() + 0.1
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        if faces:
            for x, y, w, h in faces:
                img = cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0),2)
        cv2.imshow('face_detection', img)
        if cv2.waitKey(20) & 0xFF == 27: break
    cap.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
    detect_face()
