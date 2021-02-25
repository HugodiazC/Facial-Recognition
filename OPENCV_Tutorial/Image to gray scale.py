import cv2
import numpy as np

img = cv2.imread("Resourses/INSTA_L.jpg")
Kernel = np.ones((5,5),np.uint8)

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Codigo para hacerla blanco y negro
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0) #nombre de la imagen, que tanto blur
imgCanny= cv2.Canny(img,100,100) #efecto en negros
imgDialation = cv2.dilate(imgCanny,Kernel,iterations=1) #Dilatar líneas de la imagen
imgEroded = cv2.erode(imgDialation, Kernel, iterations=1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("BLUR Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)
