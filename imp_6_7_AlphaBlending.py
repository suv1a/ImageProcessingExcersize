# alpha채널을 이용한 영상 합성

import cv2
import sys
import numpy as np

src = cv2.imread('images/kitten.jpg', cv2.IMREAD_COLOR)

# alpha채널을 포함한 4채널 컬러영상을 읽을 때는 cv2.IMREAD_UNCHANGED
logo = cv2.imread('images/opencv_logo.png', cv2.IMREAD_UNCHANGED)   

if src is None or logo is None:
    print('영상 읽기 실패')
    sys.exit()
    
# mask는 알파 채널로 만든 마스크 영상
# 그레이스케일이어야 하므로 3마지막 값만 갖고 와서 1차원으로 만들어준다.
mask = logo[:, :, 3]

# logo는 b, g, r 3채널로 구성된 컬러, 4채널이므로 -1 까지 갖고옴
logo = logo[:, :, :-1]

h, w = mask.shape[:2]

# src와 dst의 크기가 다르다. 따라서 마스크 연산이 안됌
# src와 동일한 크기의 영상을 추출 = crop
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출, 좌표는 임의대로

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0] # bool 인덱싱도 이용 가능

# cv2.imshow('Original', src)
cv2.imshow('OpenCv', logo)
cv2.imshow('mask', mask)
cv2.imshow('Result', src)
cv2.waitKey()
cv2.destroyAllWindows()