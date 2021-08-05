# Image Sharpening

import cv2
import sys
import numpy as np

# img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)
#img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)
img = cv2.imread('images/car.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()
    
# kernel = np.array([[0., -1., 0.], [-1., 5., -1.], [0., -1., 0.]])
kernel1 = np.array([[0, -1, 0], 
                   [-1, 5, -1], 
                   [0, -1, 0]])
result1 = cv2.filter2D(img, -1, kernel1)

kernel2 = np.array([[-1, -1, -1], 
                   [-1,  9, -1], 
                   [-1, -1, -1]])
result2 = cv2.filter2D(img, -1, kernel2)

cv2.imshow('Original', img)
cv2.imshow('Result1', result1)
cv2.imshow('Result2', result2)
cv2.waitKey()
cv2.destroyAllWindows()