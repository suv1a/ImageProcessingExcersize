# Laplacian, LoG

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

lap = cv2.Laplacian(img, cv2.CV_64F)
gs = cv2.GaussianBlur(img, (5,5), 0)

log = cv2.Laplacian(gs, cv2.CV_64F)

cv2.imshow('Original', img)
cv2.imshow('Laplacian', lap)
cv2.imshow('LoG', log)
cv2.waitKey()
cv2.destroyAllWindows()