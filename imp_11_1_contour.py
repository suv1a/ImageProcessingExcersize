# 영상 내 객체의 contour를 찾는다.

import cv2 as cv
import numpy as np
import random as rng

rng.seed(12345)

# 임계값에 따라 contour를 찾는다.
def thresh_callback(val):
    threshold = val
    # Canny 경계선(edge) 찾기, 임계값으로 최소, 최대정함
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    # contour 찾기
    contours, hierarchy = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # contours 그리기
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(drawing, contours, i, color, 2, cv.LINE_8, hierarchy, 0)
    
    cv.imshow('Contours', drawing)
    #cv.imwrite('contour.jpg', drawing)
    

src = cv.imread('images/shapes.png')
if src is None:
    print('Could not open or find the image:')
    exit(0)
    
# 그레이 영상으로 바꾸고, 흐림연산 수행
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))

# 창을 만들어 영상 보여주기
source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)

max_thresh = 255
thresh = 100 # 초기 임계값
# 트랙바 만들기
cv.createTrackbar('Canny Thresh:', source_window, thresh, max_thresh, thresh_callback)

# 마우스로 지정한 임계값으로 contour 찾기 호출
thresh_callback(thresh)

cv.waitKey()