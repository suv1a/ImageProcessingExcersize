# 영상의 모자이크

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

rate = 15               # 모자이크에 사용할 축소 비율 (1/rate)
win_title = 'Mosaic'    # 창 제목

while True:
    x,y,w,h = cv2.selectROI(win_title, img, False) # 관심영역 선택
    if w and h:
        roi = img[y:y+h, x:x+w]   # 관심영역 지정
        roi = cv2.resize(roi, (w//rate, h//rate), \
            interpolation=cv2.INTER_LINEAR_EXACT) # 1/rate 비율로 축소
        # 원래 크기로 확대
        roi = cv2.resize(roi, (w,h), interpolation=cv2.INTER_AREA)  
        img[y:y+h, x:x+w] = roi   # 원본 이미지에 적용
        cv2.imshow(win_title, img)
        #cv2.imwrite('moLenna.jpg', img)
    else:
        break

cv2.destroyAllWindows()