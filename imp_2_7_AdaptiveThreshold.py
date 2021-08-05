# Adaptive Thresholding
import cv2
import numpy as np

img = cv2.imread('images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)

blk_size = 9    # 블럭 사이즈
C = 5           # 차감 상수
ret, img_otsu  = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 
img_a1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, blk_size, C)
img_a2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, C)

cv2.imshow('Results Otsu', img_otsu)
cv2.imshow('Results Adaptive1', img_a1)
cv2.imshow('Results Adaptive2', img_a2)

cv2.waitKey(0)
cv2.destroyAllWindows()