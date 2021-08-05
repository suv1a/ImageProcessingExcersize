# convolution 필터 적용으로 영상 흐림

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

size = 7    
kernel = np.ones((size, size), dtype=np.float64) / (size*size)
result = cv2.filter2D(img, -1, kernel)

cv2.imshow('Original', img)
cv2.imshow('Result', result)
cv2.waitKey()
cv2.destroyAllWindows()