# 컬러영상을 읽고 산술연산을 실습한다.
import cv2
import numpy as np

img = cv2.imread('images/scene2.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Image Processing', img)

img_plus = cv2.add(img, (50,50,50,0))    # cv2연산은 saturated 연산이어서 255보다 크면 255로 고정됨
img_minus = cv2.subtract(img, (50,50,50,0))    # cv2연산은 saturated 연산이어서 0보다 작으면 0으로 고정됨
img_mul = cv2.multiply(img,(2,2,2,0))
img_div = cv2.divide(img,(2,2,2,0))

# opencv에는 이외에도 max(), min(), minMaxLoc(), 
# bitwise_and(), bitwise_or() 등 다양한 함수를 제공한다.

cv2.imshow('ResultsP', img_plus)
cv2.imshow('ResultsM', img_minus)
cv2.imshow('ResultsMu', img_mul)
cv2.imshow('ResultsD', img_div)

cv2.waitKey(0)
cv2.destroyAllWindows()