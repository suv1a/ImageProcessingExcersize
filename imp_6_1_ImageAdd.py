# 영상 단순 덧셈

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

# np.array는 [rows, colums]로 구성되므로, [height, width] 구성임에 주의!
h, w = img.shape[:2]    # 영상의 높이와 넓이 구하기
mask = np.zeros((w, h), dtype=np.uint8)  # 배경은 검정색(0)
mask = cv2.circle(mask, (w//2, h//2), h//4, (255,255,255), cv2.FILLED) # 흰색 원 그리기
mask = 255 - mask   # 마스킹할 부분을 흰 색으로

mask = cv2.imread('images/circle.png', cv2.IMREAD_GRAYSCALE)
dst = cv2.add(img, mask)

cv2.imshow('Original', img)
cv2.imshow('Mask', mask)
cv2.imshow('Result', dst)
cv2.waitKey()
cv2.destroyAllWindows()