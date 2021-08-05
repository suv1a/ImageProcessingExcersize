# Sobel, Scharr Edge Detection

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

sx = cv2.Sobel(img, -1, 1, 0, 3)
sy = cv2.Sobel(img, -1, 0, 1, 3)
resultS = cv2.add(sx, sy)


hx = cv2.Scharr(img, -1, 1, 0)
hy = cv2.Scharr(img, -1, 0, 1)
resultH = cv2.add(hx, hy)

cv2.imshow('Original', img)
cv2.imshow('Scharr', resultH)
cv2.imshow('Sobel', resultS)
cv2.waitKey()
cv2.destroyAllWindows()