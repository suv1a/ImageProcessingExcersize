# 열림 연산의 응용

import cv2
import sys
import numpy as np

src = cv2.imread('images/cell.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상 읽기 실패')
    sys.exit()

# 이진화로 노이즈 제거
ret, bin = cv2.threshold(src, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) 
# cv2.imwrite('cell_bin.jpg', bin)

# 열림연산으로 셀 분리
se = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
dst = cv2.morphologyEx(bin, cv2.MORPH_OPEN, se, iterations=1) 
# cv2.imwrite('cell_open.jpg', dst)

# 셀의 개수 세기
cnt, labels = cv2.connectedComponents(dst)

print('세포의 개수 = ', cnt)

cv2.imshow('Original1', src)
cv2.imshow('Result', dst)
cv2.waitKey()
cv2.destroyAllWindows()