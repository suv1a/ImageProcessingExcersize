# 영상 가중 덧셈(Image Blending)

import cv2
import sys
import numpy as np

img1 = cv2.imread('images/baboon.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('영상 읽기 실패')
    sys.exit()

a = 0.3     # 가중치
dst = cv2.addWeighted(img1, a, img2, 1-a, 0)

cv2.imshow('Original', img1)
cv2.imshow('Image', img2)
cv2.imshow('Result', dst)
cv2.waitKey()
cv2.destroyAllWindows()