# Chroma key를 이용한 영상 합성

import cv2
import sys
import numpy as np

src = cv2.imread('images/green_chroma_key.jpg', cv2.IMREAD_COLOR)
bg = cv2.imread('images/bg2.jpg', cv2.IMREAD_COLOR)
if src is None or  bg is  None:
    print('영상 읽기 실패')
    sys.exit()
    
# HSV 색 공간에서 녹색 영역을 검출
hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, (50, 100, 0), (80, 255, 255)) # 최솟값, 최댓값
                    # hue: green(50,80), saturation: 100이상, value는 무시
# 녹색 영역에 다른 영역 배경을 합성하기
cv2.copyTo(bg, mask, src)

# cv2.imshow('Original', src)
cv2.imshow('mask', mask)
#cv2.imwrite('chroma_mask.jpg', mask)
cv2.imshow('Result', src)
#cv2.imwrite('chroma_res.jpg', src)
cv2.waitKey()
cv2.destroyAllWindows()