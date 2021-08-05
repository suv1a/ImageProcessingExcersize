# Edge Detection

import cv2
import sys
import numpy as np

img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('영상 읽기 실패')
    sys.exit()

PrewittX = np.array([[-1, -1, -1], 
                   [0, 0, 0], 
                   [1, 1, 1]])
PrewittY = np.array([[1, 0, -1], 
                   [1, 0, -1], 
                   [1, 0, -1]])

RobertsX = np.array([[-1, 0, 0], 
                   [0, 1, 0], 
                   [0, 0, 0]])
RobertsY = np.array([[0, 0, -1], 
                   [0, 1, 0], 
                   [0, 0, 0]])

SobelX = np.array([[-1, -2, -1], 
                   [0, 0, 0], 
                   [1, 2, 1]])
SobelY = np.array([[1, 0, -1], 
                   [2, 0, -2], 
                   [1, 0, -1]])

px = cv2.filter2D(img, -1, PrewittX)
py = cv2.filter2D(img, -1, PrewittY)
resultP = cv2.add(px, py)

rx = cv2.filter2D(img, -1, RobertsX)
ry = cv2.filter2D(img, -1, RobertsY)
resultR = cv2.add(rx, ry)

sx = cv2.filter2D(img, -1, SobelX)
sy = cv2.filter2D(img, -1, SobelY)
resultS = cv2.add(sx, sy)

cv2.imshow('Original', img)
cv2.imshow('Prewitt', resultP)
cv2.imshow('Roberts', resultR)
cv2.imshow('Sobel', resultS)
cv2.waitKey()
cv2.destroyAllWindows()