# Morpholoy erosion

import cv2
import sys
import numpy as np

white = (255, 255, 255)
black = (0, 0, 0)

src = np.zeros((256, 512), dtype=np.uint8)  # 배경은 검정색(0)
src = cv2.rectangle(src, (60, 60), (196,196), white) # 흰색 사각형 그리기
src = cv2.circle(src, (384, 128), 70, white, cv2.FILLED) # 흰색 채운 원 그리기
src = cv2.line(src, (314, 128), (384, 128), black) # 검은 직선 그리기
src = cv2.line(src, (244, 128), (314, 128), white) # 흰 직선 그리기

# se = np.ones((3,3), np.uint8)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

ero = cv2.morphologyEx(src, cv2.MORPH_ERODE, se)
dil = cv2.morphologyEx(src, cv2.MORPH_DILATE, se)
ope = cv2.morphologyEx(src, cv2.MORPH_OPEN, se)
clo = cv2.morphologyEx(src, cv2.MORPH_CLOSE, se)
gra = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, se)
th  = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, se)
bh  = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, se)

cv2.imshow('Original', src)
cv2.imshow('Erosion', ero)
cv2.imshow('Dialation', dil)
cv2.imshow('Opening', ope)
cv2.imshow('Gradient', gra)
cv2.imshow('Closing', clo)
cv2.imshow('Top Hat', th)
cv2.imshow('Black Hat', bh)
cv2.waitKey()
cv2.destroyAllWindows()