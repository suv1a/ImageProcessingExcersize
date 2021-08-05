# 물체의 외접 최소 사각형, 타원 구하기

import cv2 as cv
import numpy as np
import random as rng
rng.seed(12345)

def thresh_callback(val):
    threshold = val    
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)        
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # 각 contour의 회전된 외접 사각형과 타원을 구한다.
    minRect = [None]*len(contours)
    minEllipse = [None]*len(contours)
    for i, c in enumerate(contours):
        minRect[i] = cv.minAreaRect(c)
        if c.shape[0] > 5:
            minEllipse[i] = cv.fitEllipse(c)
    
    # 결과 출력    
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
    for i, c in enumerate(contours):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        # contour
        cv.drawContours(drawing, contours, i, color)
        # ellipse
        if c.shape[0] > 5:
            cv.ellipse(drawing, minEllipse[i], color, 2)
        # rotated rectangle
        box = cv.boxPoints(minRect[i])
        box = np.intp(box) #np.intp: Integer used for indexing (same as C ssize_t; normally either int32 or int64)
        cv.drawContours(drawing, [box], 0, color)    
    
    cv.imshow('Bounding Box and Ellipse', drawing)
    cv.imwrite('Rotated BB.jpg', drawing)
    
src = cv.imread('images/balloons.jpg')
if src is None:
    print('Could not open or find the image.')
    exit(0)
    
# Convert image to gray and blur it
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))

source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)

max_thresh = 255
thresh = 100 # initial threshold
cv.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)

thresh_callback(thresh)
cv.waitKey()