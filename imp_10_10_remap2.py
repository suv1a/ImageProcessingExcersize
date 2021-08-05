# 영상의 비선형 remapping

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

h, w  = img.shape[:2]

# 기초 매핑 배열 생성
mapy, mapx = np.indices((h, w), dtype=np.float32)

l = 20      # 파장(wave length)
amp = 15    # 진폭(amplitude)
# sin, cos 함수를 적용한 변형 매핑 연산
sinx = mapx + amp * np.sin(mapy/l)  
cosy = mapy + amp * np.cos(mapx/l)

# 영상 매핑
img_sinx=cv2.remap(img, sinx, mapy, cv2.INTER_LINEAR) # x축만 sin 곡선 적용
img_cosy=cv2.remap(img, mapx, cosy, cv2.INTER_LINEAR) # y축만 cos 곡선 적용
# x,y 축 모두 sin, cos 곡선 적용 및 외곽 영역 보정
# img_both=cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR)
img_both=cv2.remap(img, sinx, cosy, cv2.INTER_LINEAR, \
                    None, cv2.BORDER_REPLICATE)

cv2.imshow('Original', img)
cv2.imshow('Remap Sin x', img_sinx)
cv2.imshow('Remap Cos y', img_cosy)
cv2.imshow('Remap Both', img_both)
#cv2.imwrite('dtLenna.jpg', img_both)

cv2.waitKey()
cv2.destroyAllWindows()