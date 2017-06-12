import cv2
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('news.jpg', 1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor=1.05,
    minNeighbors=5
)

for x, y, width, height in faces:
    img = cv2.rectangle(
        img,
        (x, y), # top left coordenated
        (x+width, y+height), # bottom right coordinates
        (0, 255, 0), # color RGB
        3 # rectangle width
    )

plt.imshow(img, cmap='gray')
plt.show()

cv2.imwrite('test.jpg', img)
