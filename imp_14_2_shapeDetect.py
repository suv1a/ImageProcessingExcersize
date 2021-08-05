# 도형 이름 맞추기

import cv2
import math
import sys
import numpy as np

# 사각형을 그리고 결과를 출력하는 함수
def setLabel(img, pts, label):
    # 사각형 좌표 받아오기
    (x, y, w, h) = cv2.boundingRect(pts)
    pt1 = (x, y)
    pt2 = (x + w, y + h)
    cv2.rectangle(img, pt1, pt2, (0, 0, 255), 1)
    cv2.putText(img, label, pt1, cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0))

# 두 벡터 사이의 각도 구하기
# x축과 이루는 각도의 차이를 이용함(방향에 주의)
def calcAngle2V(a, b):
    ang_1 = np.arctan2(*a[::-1])
    ang_2 = np.arctan2(*b[::-1])
    ang = np.rad2deg((ang_1 - ang_2) % (2*np.pi))
    return ang
def calcAngle3P(a, b, c):
    ba = a - b
    bc = c - b
    return calcAngle2V(bc[0], ba[0])

# 외적(cross product)의 크기는 |a||b|sin(theta),
# 내적(inner produc)는 |a||b|cos(theta)를 이용하여 각도계산
# 각도의 방향은 오른손 법칙을 따름
def calcAngle2(a, b):
    dot = np.dot(a, b)
    cross = np.cross(a, b)
    angle = np.arctan2(cross, dot)
    return np.rad2deg(angle % (2*np.pi))

# 세 점 사이의 각도 구하기
def calcAngle3(a, b, c):
    ba = a - b
    bc = c - b
    return calcAngle2(ba[0], bc[0])

    
img = cv2.imread('images/shapes2.png', cv2.IMREAD_COLOR)
    
if img is None:
    print('Image load failed!')
    sys.exit()

cv2.imshow('Source', img)

# 그레이스케일 영상으로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이진화, INV 이유는 배경이 흰색, 객체가 어두운 영상이므로
_, img_bin = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# 외곽선 검출, EXTERNAL로 바깥 외곽선만 도출
contours, _ = cv2.findContours(img_bin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# 외곽선 좌표 받아오기
for pts in contours:
    if cv2.contourArea(pts) < 400: # 노이즈 제거, 너무 작으면 무시
        continue
    
    # 근사화
    approx = cv2.approxPolyDP(pts, cv2.arcLength(pts, True)*0.02, True)
    
    # 근사화 결과 점 갯수
    vtc = len(approx)
    
    # 점 사이의 각도를 구하여 더한다.
    ang_sum = 0
    size = vtc
    
    for k in range(size):
        ang = calcAngle3P(approx[k], approx[(k+1)%size], approx[(k+2)%size])
        ang_sum = ang_sum + ang
    
    # 다각형 내각의 합은 180 * (n - 2)
    threshold = 8 # 
    ang_sum_min = (180 - threshold) * (size - 2) 
    ang_sum_max = (180 + threshold) * (size - 2)
        
    # 3이면 삼각형
    if vtc == 3:
        setLabel(img, pts, 'TRIANGLE')
    # 4면 사각형
    elif vtc == 4 and ang_sum >= ang_sum_min and ang_sum <= ang_sum_max:
        setLabel(img, pts, 'RECTANGLE')
    elif vtc == 5 and ang_sum >= ang_sum_min and ang_sum <= ang_sum_max:
        setLabel(img, pts, 'PENTAGON')
    elif vtc == 6 and ang_sum >= ang_sum_min and ang_sum <= ang_sum_max:
        setLabel(img, pts, 'HEPTAGON')
    else:
        length = cv2.arcLength(pts, True)
        area = cv2.contourArea(pts)
        ratio = 4. * math.pi * area / (length * length)

        if ratio > 0.85:
            setLabel(img, pts, 'CIRCLE')
        else:
            setLabel(img, pts, str(size)+'-Pts')

cv2.imshow('Results', img)
cv2.waitKey()
cv2.destroyAllWindows()
