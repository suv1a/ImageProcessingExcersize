# 영상의 단순 확대

import cv2
import sys
import numpy as np

img = cv2.imread('images/baboon.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

h, w = img.shape[:2]    # 영상의 높이(rows)와 넓이(columns) 구하기
sx = 3     # x축 확대 크기
sy = 2       # y축 확대 크기
M = np.float64([[sx, 0, 0], [0, sy, 0]]) 
# 최근접이웃 보간
dst = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_NEAREST)

cv2.imshow('Original', img)
cv2.imshow('Result', dst)
cv2.waitKey()
cv2.destroyAllWindows()