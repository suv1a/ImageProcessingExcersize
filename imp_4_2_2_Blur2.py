# blur()함수로 영상 흐림

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()
    
result3 = cv2.blur(img, (3,3))
result5 = cv2.blur(img, (5,5))

cv2.imshow('Original', img)
cv2.imshow('Result3', result3)
cv2.imshow('Result5', result5)
cv2.waitKey()
cv2.destroyAllWindows()