# 허프변환으로 직선 찾기

import sys
import math
import cv2 as cv
import numpy as np

# Loads an image
src = cv.imread('images/sudoku.jpg', cv.IMREAD_GRAYSCALE)

# Check if image is loaded fine
if src is None:
    print ('Error opening image!')
    sys.exit()

# Canny edge detection    
dst = cv.Canny(src, 50, 200, None, 3)
    
# Copy edges to the images that will display the results in BGR
cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
cdstP = np.copy(cdst)

# 기본 허프변환, rho=1 픽셀, theta=1 degree, threshold=150(최소 교차 수)
# 반환값은 찾은 직선의 (rho, theta)
lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

# 찾은 직선을 붉은색으로 그려준다.    
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

# 확률적 허프 변환 적용, 최소길이 50, 조사할 같은 직선의 두 점의 최대 거리 10
# 반환값은 직선의 시점과 끝점 (x_start, y_start, x_end, y_end)
linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)

# 결과 출력    
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
    
cv.imshow("Source", src)
cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    
cv.waitKey()
