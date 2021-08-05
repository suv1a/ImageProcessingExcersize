# 톱햇 연산의 응용

import cv2
import sys
import numpy as np

src = cv2.imread('images/light.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상 읽기 실패')
    sys.exit()

# 그냥 이진화
ret, bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

# 톱햇 후 이진화, 구조요소는 물체를 찾을 수 있게 충분히 커야 함
se = cv2.getStructuringElement(cv2.MORPH_RECT, (13,13))
th = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, se) 
ret, dst = cv2.threshold(th, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 


cv2.imshow('Original1', src)
cv2.imshow('Result1', bin)
cv2.imshow('Top Hat', th)
cv2.imshow('Result2', dst)
cv2.waitKey()
cv2.destroyAllWindows()