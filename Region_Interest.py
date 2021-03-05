import cv2
import pickle

face_cascade = cv2.CascadeClassifier("Resourses/cascades/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()

cap= cv2.VideoCapture(0)

while(True):
    ret,frame = cap.read()
    #Capture frame by frame
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    for (x, y, w, h) in faces:
        print(x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]  # (cord1-height, cord2-height)
        img_item = "Prueba.png"
        cv2.imwrite(img_item, roi_gray)

    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#When everything done, release teh capture
cap.release()
cv2.destroyAllWindows()