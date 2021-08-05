# 영상의 회전

import cv2
import sys
import math
import numpy as np

img = cv2.imread('images/baboon.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

theta = 25  # 회전 각도
rad = theta * math.pi / 180
M = np.array([[math.cos(rad), math.sin(rad), 0],
              [-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)
dst = cv2.warpAffine(img, M, (0,0))

cv2.imshow('Original', img)
cv2.imshow('Result1', dst)
cv2.waitKey()
cv2.destroyAllWindows()