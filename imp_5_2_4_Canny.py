# Canny Edge Detection

import cv2
import sys
import numpy as np

# img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/balloons.jpg', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

be = cv2.Canny(img[:,:,0], 80, 150)
ge = cv2.Canny(img[:,:,1], 80, 150)
re = cv2.Canny(img[:,:,2], 80, 150)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cn = cv2.Canny(gray, 80, 150)

cv2.imshow('Original', img)
cv2.imshow('Blue',img[:,:,0])
cv2.imshow('Green',img[:,:,1] )
cv2.imshow('Red', img[:,:,2])
cv2.imshow('Blue Edge', be)
cv2.imshow('Green Edge', ge)
cv2.imshow('Red Edge', re)
cv2.imshow('Gray', gray)
cv2.imshow('Canny', cn)
cv2.waitKey()
cv2.destroyAllWindows()