# Thresholding
import cv2
import numpy as np

img = cv2.imread('images/apples.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('Image Processing', img)

ret, img_binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # 127임계값, 255 픽셀값
# 최적의 임계값을 찾아주는 otsu의 알고리즘 적용
ret, img_otsu  = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) 

cv2.imshow('ResultsB', img_binary)
cv2.imshow('ResultsO', img_otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()