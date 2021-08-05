# 영상의 스케일링(확대, 축소)

import cv2
import sys
import numpy as np

img = cv2.imread('images/baboon.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

# 확대: cubic convolution 보간
dst1 = cv2.resize(img, (0,0), fx=3, fy=2, interpolation=cv2.INTER_CUBIC)
# 축소: AREA-축소될 지역의 픽셀값을 평균함
dst2 = cv2.resize(img, (0,0), fx=0.55, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow('Original', img)
cv2.imshow('Result1', dst1)
cv2.imshow('Result2', dst2)
cv2.waitKey()
cv2.destroyAllWindows()