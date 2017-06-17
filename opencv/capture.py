import cv2
import matplotlib.pyplot as plt

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    plt.imshow(frame, cmap='gray')
    plt.pause(0.01)
    plt.draw()
    key = plt.waitforbuttonpress(0.01)

    if key:
        break;

video.release()
