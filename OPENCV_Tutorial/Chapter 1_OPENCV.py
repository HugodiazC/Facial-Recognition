import cv2
print ("Packege Imported")

#leer imagenes
img = cv2.imread( """ANEXA RUTA Y NOMBRE DE TU ARCHIVO, SAMPLE: "Resourses/Daniela.jpg" """)

cv2.imshow("Output", img) #(primer parametro nombre de la ventada, segundo imagen a mostrar)
cv2.waitKey(0) #demorar unos segundos la ventana

#Importar vídeo
cap=cv2.VideoCapture( """AANEXA RUTA Y NOMBRE DE TU ARCHIVO, SAMPLE: "Resourses/Sleeping Concert_ART" """)

while True:
    success,img =cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break


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

#Manipular imágenes, hacerlas blanco y negro, filtros etc.
import cv2
import numpy as np

img = cv2.imread("""ANEXA RUTA Y NOMBRE DE TU ARCHIVO, SAMPLE: "Resourses/Daniela.jpg" """)
Kernel = np.ones((5,5),np.uint8)

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Código para hacerla blanco y negro
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0) #nombre de la imagen, settings del blur
imgCanny= cv2.Canny(img,100,100) #efecto en negros
imgDialation = cv2.dilate(imgCanny,Kernel,iterations=1) #Dilatar líneas de la imagen
imgEroded = cv2.erode(imgDialation, Kernel, iterations=1)


cv2.imshow("Gray Image", imgGray)
cv2.imshow("BLUR Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

#Resahpe and Cropp image
img = cv2.imread("""ANEXA RUTA Y NOMBRE DE TU ARCHIVO, SAMPLE: "Resourses/Daniela.jpg" """)
print(img.shape) # para saber el tamaño actual

imgResize=cv2.resize(img,(300,200)) # para asignar un nuevo tamaño a la imagen

imgCropped=img[0:200,200:500] # high firts/ esto es para cortar imágenes

cv2.imshow("imagen normal",img)
cv2.imshow("imagen resize",imgResize)
cv2.imshow("imagen Croped",imgCropped)

cv2.waitKey(0)
