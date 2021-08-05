# 영상 합성

import cv2
import sys
import numpy as np

src = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)
mask = cv2.imread('images/Lenna_mask.png', cv2.IMREAD_COLOR)
dst = cv2.imread('images/flowers-413.jpg', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('영상 읽기 실패')
    sys.exit()

cv2.copyTo(src, mask, dst)
cv2.imshow('Original', src)
cv2.imshow('mask', mask)
cv2.imshow('Result', dst)

cv2.waitKey()
cv2.destroyAllWindows()