# 영상의 중앙기준 회전, 크기 조정

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
(cx, cy) = (w//2, h//2) # 중심점 좌표

# sin, cos 값 구하기 + 중앙점 변환 행렬 구하기
M = cv2.getRotationMatrix2D((cx,cy), theta, 1.0)
cos = np.abs(M[0,0])
sin = np.abs(M[0,1])

# 회전한 영상의 크기 구하기
nW = int((h*sin) + (w*cos))
nH = int((h*cos)  + (w*sin))

# 확대된 크기에 맞게 변환행렬 수정
M[0,2] = M[0,2] + (nW / 2) - cx
M[1,2] = M[1,2] + (nH / 2)  - cy

dst = cv2.warpAffine(img, M, (nW,nH))

cv2.imshow('Original', img)
cv2.imshow('Result1', dst)
cv2.waitKey()
cv2.destroyAllWindows()