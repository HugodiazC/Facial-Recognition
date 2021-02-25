import cv2
import numpy as np

#img= np.zeros((512,512)) #los zeros son negros los unos son blanco
#Resultado de esto imagen completamente negra.

#img2= np.zeros((512,512,3),np.uint8) # esto es para imagen a color
#img3= np.zeros((512,512,3),np.uint8)
img4= np.zeros((512,512,3),np.uint8)
#print(img2)
#img2[:]=255,0,0 #esto la pinta de azul
#img3[200:300,100:300]=255,0,0 #esto la pinta de azul

cv2.line(img4,(0,0),(300,300),(0,255,0),3)

#cv2.imshow("image 1",img)
#cv2.imshow("image",img2)
#cv2.imshow("image 3",img3)
cv2.imshow("image 4",img4)

cv2.waitKey(0)

