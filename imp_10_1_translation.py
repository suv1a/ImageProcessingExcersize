# 영상의 이동

import cv2
import sys
import numpy as np

img = cv2.imread('images/baboon.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

h, w = img.shape[:2]    # 영상의 높이(rows)와 넓이(columns) 구하기
dx = 100     # x축 이동 크기
dy = 200     # y축 이동 크기
M = np.float64([[1, 0, dx], [0, 1, dy]])    # 변환행렬
dst = cv2.warpAffine(img, M, (w, h))

cv2.imshow('Original', img)
cv2.imshow('Result', dst)
cv2.waitKey()
cv2.destroyAllWindows()