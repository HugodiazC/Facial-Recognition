import cv2

img = cv2.imread("Resourses/INSTA_L.jpg")
print(img.shape) # para saber el tamaño actual

imgResize=cv2.resize(img,(300,200)) # para asignar un nuevo tamaño a la imagen

imgCropped=img[0:200,200:500] # high firts/ esto es para cortar imágenes

cv2.imshow("imagen normal",img)
cv2.imshow("imagen resize",imgResize)
cv2.imshow("imagen Croped",imgCropped)

cv2.waitKey(0)
