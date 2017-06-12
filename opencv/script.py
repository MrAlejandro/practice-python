import cv2
import matplotlib.pyplot as plt

# 1 - for colored image
# 2 - for black and white
# 3 - for colored image + alpha channel (transparensy capabilities)
img = cv2.imread('galaxy.jpg', 0)

print(img.shape) # size of the image
print(img.ndim) # number of dimentions of an array

# show the window with an image
# cv2.imshow('Galaxy', img) # not working on Mac
# cv2.waitKey(3) # not working on Mac
# cv2.destroyAllWindows()

resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imwrite('resized.jpg', resized_image)
# another (working) way do display an image right from python
# plt.imshow(resized_image, cmap='gray')
# plt.show()
