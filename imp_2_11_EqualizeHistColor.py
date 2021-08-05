# 컬러영상의 히스토그램 평활화

import cv2
import numpy as np
import matplotlib.pylab as plt

# 컬러영상 읽기
img = cv2.imread('images/cute.jpg', cv2.IMREAD_COLOR)

# 컬러공간을 HSV로 변경
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# V(밝기값) 공간에 히스토그램 평활화 적용
img_hsv[:,:,2] = cv2.equalizeHist(img_hsv[:,:,2])

# 컬러공간을 RGB로 원위치
img2 = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2BGR)
b, g, r = cv2.split(img)
b = cv2.equalizeHist(b)
g = cv2.equalizeHist(g)
r = cv2.equalizeHist(r)
img3 = cv2.merge((b,g,r))

# 결과 출력
cv2.imshow('Before', img)
cv2.imshow('After', img2)
cv2.imshow('RGB', img3)
cv2.waitKey()
cv2.destroyAllWindows()