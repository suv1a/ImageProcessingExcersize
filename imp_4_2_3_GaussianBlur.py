# GaussianBlur()함수로 영상 흐림

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

# sigma 지정    
result1 = cv2.GaussianBlur(img, (0,0), 1)
result3 = cv2.GaussianBlur(img, (0,0), 3)

# ksize 지정, mean smoothing과 비교
resultB = cv2.blur(img, (5,5))
resultG = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow('Original', img)
cv2.imshow('Result_S_1', result1)
cv2.imshow('Result_S_3', result3)
cv2.imshow('Result_mean', resultB)
cv2.imshow('Result_Gaussian', resultG)
cv2.waitKey()
cv2.destroyAllWindows()