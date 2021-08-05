# Bilateral Filtering
# 경계선(에지)을 보존하면서 노이즈를 감소시킴
# cv2.bilateralFilter(src, d, sigmaColor, simgaSpace)
# d: 이웃 픽셀 거리, -1이면 자동계산
# sigmaColor: 색 공간 표준 편차
# sigmaSpace: 좌표 공간 표준편차

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)
# img = cv2.imread('images/pns_color.jpg', cv2.IMREAD_COLOR)
# img = cv2.imread('images/Multiplicative-Gaussian-Noise.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

resultB = cv2.bilateralFilter(img, 9, 75, 75)
# ksize 지정, mean smoothing과 비교
resultM = cv2.blur(img, (5,5))
resultG = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow('Original', img)
cv2.imshow('Result_bilateral', resultB)
cv2.imshow('Result_mean', resultM)
cv2.imshow('Result_Gaussian', resultG)
cv2.waitKey()
cv2.destroyAllWindows()