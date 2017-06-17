import cv2

# img = cv2.imread('galaxy.jpg')
# cv2.imshow('Capturing', img)
# key = cv2.waitKey(0)
# cv2.destroyAllWindows()

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    print(type(frame));
    print(frame.shape);
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Capturing', gray)

    key = cv2.waitKey(1000)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
