# 영상의 remapping

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

h, w  = img.shape[:2]

# np.indice는 행렬의 인덱스값 x좌표값 y좌표값을 따로따로 행렬의 형태로 변환해줌
map2, map1 = np.indices((h, w), dtype=np.float32)

# (200, 100) 이동
map1 = map1 - 200
map2 = map2 - 100
trn = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR)

# 좌우 대칭
map2, map1 = np.indices((h, w), dtype=np.float32)
map1 = w - 1 - map1
fh = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR)


cv2.imshow('Original', img)
cv2.imshow('Remap Translation', trn)
cv2.imshow('Remap FlipH', fh)

cv2.waitKey()
cv2.destroyAllWindows()