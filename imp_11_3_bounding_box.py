# 물체를 감싸는 사각형과 원을 찾아 그린다.

import cv2 as cv
import numpy as np
import random as rng
rng.seed(12345)

def thresh_callback(val):
    threshold = val
    
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)   
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # 외접 사각형과 원을 위한 변수 선언    
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    
    for i, c in enumerate(contours): # index, contours
        contours_poly[i] = cv.approxPolyDP(c, 3, True) # 다각형 근사
        boundRect[i] = cv.boundingRect(contours_poly[i]) # 외접 사각형
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i]) # 외접 원
        
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
        
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
        cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
    
    
    cv.imshow('Bounding Box and Circle', drawing)
    #cv.imwrite('Bounding_Box_Circles.jpg', drawing)
    
src = cv.imread('images/balloons.jpg')
if src is None:
    print('Could not open or find the image')
    exit(0)
    
# 그레이 영상으로 바꾸고 노이즈 제거를 위해 블러링한다.
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))

source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)

max_thresh = 255
thresh = 100 # initial threshold
cv.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)

thresh_callback(thresh)
cv.waitKey()