# Median Filtering

import cv2
import sys
import numpy as np

# img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('images/pns.jpg', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/gnoise.jpg', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

# sigma 지정    
result3 = cv2.medianBlur(img, 3)
result5 = cv2.medianBlur(img, 5)

# ksize 지정, mean smoothing과 비교
resultB = cv2.blur(img, (5,5))
resultG = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow('Original', img)
cv2.imshow('Result_3', result3)
cv2.imshow('Result_5', result5)
cv2.imshow('Result_mean', resultB)
cv2.imshow('Result_Gaussian', resultG)
cv2.waitKey()
cv2.destroyAllWindows()