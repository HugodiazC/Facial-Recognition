import cv2
#WEBCAM connect
cap=cv2.VideoCapture(0)
cap.set(3,640) #tamaño de la imagen
cap.set(4,480)
cap.set(10,100) #para mejorar el brillo de la pantalla

while True:
    success,img =cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break