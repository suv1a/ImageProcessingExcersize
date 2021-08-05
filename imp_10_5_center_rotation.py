# 영상의 중앙기준 회전

import cv2
import sys
import math
import numpy as np

img = cv2.imread('images/baboon.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

theta = 25  # 회전 각도
h, w = img.shape[:2]
cp = (w//2, h//2)
M = cv2.getRotationMatrix2D(cp, theta, 1)
dst = cv2.warpAffine(img, M, (0,0))

cv2.imshow('Original', img)
cv2.imshow('Result1', dst)
cv2.waitKey()
cv2.destroyAllWindows()