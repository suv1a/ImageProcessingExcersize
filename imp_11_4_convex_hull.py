# convex hull 찾기

import cv2 as cv
import numpy as np

import random as rng
rng.seed(12345)

def thresh_callback(val):
    threshold = val
    # Canny 경계선 찾기
    canny_output = cv.Canny(src_gray, threshold, threshold * 2)
    # Contour 찾기
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    # 각 윤곽선(contour)의 볼록껍질(convex hull 찾기
    hull_list = []
    for i in range(len(contours)):
        hull = cv.convexHull(contours[i])
        hull_list.append(hull)
    # Contour와 Convex Hull 그리기
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(drawing, contours, i, color)
        cv.drawContours(drawing, hull_list, i, color)
    # 결과 보이기
    cv.imshow('Convex Hull', drawing)
    #cv.imwrite('convex_hull.jpg', drawing)
    
# 영상을 읽고 프로그램 시작
src = cv.imread('images/hand.jpg')
if src is None:
    print('Could not open or find the image:')
    exit(0)

# 그레이영상으로 바꾸고, 흐림연산 수행
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
src_gray = cv.blur(src_gray, (3,3))

# 창을 만들어 입력영상 보여주기
source_window = 'Source'
cv.namedWindow(source_window)
cv.imshow(source_window, src)

max_thresh = 255
thresh = 100 # 초기 임계값
# 트랙바 만들기
cv.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)

# Convex Hull찾기 호출
thresh_callback(thresh)

cv.waitKey()