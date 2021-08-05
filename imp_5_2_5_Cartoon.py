# Cartoon 영상 만들기
# 1) 영상을 단순화 - 영상 축소 후 bilateral 필터링
# 2) 경계선 영상 생성 - Canny 호출
# 3) 단순화된 영상과 경계선 영상의 합성

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

h, w = img.shape[:2]    # 영상의 높이와 넓이 구하기
img2 = cv2.resize(img, (w//2, h//2))  # 반으로 축소(단순화)

blr = cv2.bilateralFilter(img2, -1, 20, 7)  # 과장된 효과를 위해 큰 값 지정
edge = 255 - cv2.Canny(img2, 80, 120)       # 흰색과 검정색의 반전

dst = cv2.bitwise_and(blr, edge)    # Canny 영상의 검은색(경계선)을 blr에서 강화
dst = cv2.resize(dst,  (w, h),  interpolation=cv2.INTER_NEAREST)

cv2.imshow('Original', img)
cv2.imshow('Cartoon', dst)
cv2.waitKey()
cv2.destroyAllWindows()