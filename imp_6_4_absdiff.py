# 영상 뺄셈

import cv2
import sys
import numpy as np

img1 = cv2.imread('images/diff1.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('images/diff2.jpg', cv2.IMREAD_COLOR)

if img1 is None  or img2 is None:
    print('영상 읽기 실패')
    sys.exit()

dst = cv2.absdiff(img1, img2)   # 영상의 차이ㅣ 구하기
ret, bin = cv2.threshold(dst, 30, 255, cv2.THRESH_BINARY) # 차이를 강화
ans = cv2.absdiff(img1, bin)    # 원래 영상에 표시

cv2.imshow('Original1', img1)
cv2.imshow('Original2', img2)
cv2.imshow('Result', dst)
cv2.imshow('ans', ans)
cv2.waitKey()
cv2.destroyAllWindows()