# 그레이영상을 읽고, 특정 픽셀 값을 읽고, 바꾸어 본다.

import cv2
import numpy as np

img = cv2.imread('images/scene2.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)

print(img.shape)
px = img[100,100]
print(px)
img[100:110,100:110] = 0

cv2.imshow('Results', img)
cv2.waitKey(0)
cv2.destroyAllWindows()