# biwise and,  or,  xor, not
# gray image에서 밝기 0은  이진수 0, 밝기가 0이 아니면 이진수 1
# gray image에서 이진수 1은 밝기가 255임

import cv2
import sys
import numpy as np

img1 = np.zeros((300, 300), dtype=np.uint8)  # 배경은 검정색(0)
img2 = np.zeros((300, 300), dtype=np.uint8)  # 배경은 검정색(0)
img1 = cv2.circle(img1, (150,150), 150, 255, -1) # 흰색 원 그리기
img2 = cv2.rectangle(img2, (25,25), (275,275), 255,-1) # 흰색 사각형 그리기

bAnd = cv2.bitwise_and(img1, img2)
bOr = cv2.bitwise_or(img1, img2)
bXor = cv2.bitwise_xor(img1, img2)
bNot = cv2.bitwise_not(img1)

cv2.imshow('Circle', img1)
cv2.imshow('Rectangle', img2)
cv2.imshow('AND', bAnd)
cv2.imshow('OR', bOr)
cv2.imshow('XOR', bXor)
cv2.imshow('NOT', bNot)
cv2.waitKey()
cv2.destroyAllWindows()