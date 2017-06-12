import cv2
import matplotlib.pyplot as plt

video = cv2.VideoCapture(0)

a = 0

while True:
    a += 1
    check, frame = video.read()
    plt.imshow(frame, cmap='gray')
    plt.pause(0.01)
    plt.draw()
    key = plt.waitforbuttonpress(0.001)

    if key:
        break;

print(a)
video.release()
cv2.destroyAllWindows()
