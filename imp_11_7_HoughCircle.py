# 허프변환으로 원 찾기
import sys
import cv2
import numpy as np

# Loads an image
src = cv2.imread('images/buttons.jpg', cv2.IMREAD_COLOR)
# Check if image is loaded fine
if src is None:
    print ('Error opening image!')
    sys.exit()
       
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
        
# 트랙바 함수 정의
def on_trackbar(pos):
    # 트랙바 초기값 정보 받아오기
    rmin = cv2.getTrackbarPos('minRadius', 'img')
    rmax = cv2.getTrackbarPos('maxRadius', 'img')
    th = cv2.getTrackbarPos('threshold', 'img')
    
    # 받아온 정보를 cv2.HoughCircles에 입력
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50, \
                               param1=120, param2=th, minRadius=rmin, maxRadius=rmax)
    # dp=1: 해상도의 역수, 1이면 입력과 동일
    # min_dist = 50: 중심점 사이의 최소 거리
    # param1=120: Canny 에지탐색의 상한 임계값
    # param2=th: 중심점 찾기 임계값
    # minRadius, maxRadius: 반지름의 최소, 최댓값
    # 반환값: (X_center, y_center, radius)   

    dst = src.copy() # 복사한 입력영상 위에 원 그리기
    if circles is not None:
        for i in range(circles.shape[1]): # 검출된 원 갯수만큼 반복
            cx, cy, radius = circles[0][i] # i번째 원에 데이터 저장
            cv2.circle(dst, (cx, cy), int(radius), (0, 0, 255), 2, cv2.LINE_AA) # 저장된 데이터를 이용해 원 그리기
    
    cv2.imshow('img', dst)
    #cv2.imwrite('HoughCircle.jpg', dst)
    
# 트랙바 생성
cv2.imshow('img', src)

# 트랙바 범위
cv2.createTrackbar('minRadius', 'img', 0, 100, on_trackbar)
cv2.createTrackbar('maxRadius', 'img', 0, 150, on_trackbar)
cv2.createTrackbar('threshold', 'img', 0, 100, on_trackbar)

# 트랙바 초깃값
cv2.setTrackbarPos('minRadius', 'img', 10) # 초기값 10
cv2.setTrackbarPos('maxRadius', 'img', 80)
cv2.setTrackbarPos('threshold', 'img', 40)

cv2.waitKey()

cv2.destroyAllWindows()
