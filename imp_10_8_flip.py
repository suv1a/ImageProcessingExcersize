# 영상의 대칭변환

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

# 좌우대칭
fh = cv2.flip(img, 1)
# 상하대칭
fv = cv2.flip(img, 0)
# 좌우&상하대칭
fb = cv2.flip(img, -1)


cv2.imshow('Original', img)
cv2.imshow('Flip Horizontal', fh)
cv2.imshow('Flip Vertical', fv)
cv2.imshow('Flip Both', fb)
cv2.waitKey()
cv2.destroyAllWindows()