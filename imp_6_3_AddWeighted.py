# 영상 가중 덧셈
# 트랙바 활용

import cv2
import sys
import numpy as np

img1 = cv2.imread('images/baboon.png', cv2.IMREAD_COLOR)
img2 = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('영상 읽기 실패')
    sys.exit()
    
def change(x):
    pass
cv2.namedWindow('Mixed')
cv2.createTrackbar('Weight', 'Mixed', 0, 100, change)

while True:
    weight = cv2.getTrackbarPos('Weight', 'Mixed')
    result = cv2.addWeighted(img1, float(100-weight)*0.01, img2, float(weight)*0.01, 0)
    cv2.imshow('Mixed', result)
    
    if cv2.waitKey(1) & 0xFF == 27:     # ESC로 종료
        break

cv2.waitKey()
cv2.destroyAllWindows()