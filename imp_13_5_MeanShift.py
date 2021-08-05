# MeanSift로 객체 추적

import numpy as np
import cv2 as cv

cap = cv.VideoCapture('images/data_slow.flv')

# take first frame of the video
ret,frame = cap.read()

# setup initial location of window
# r,h,c,w = 250,90,400,125  # simply hardcoded the values(손으로 지정)
r,h,c,w = 200,40,350,60  # simply hardcoded the values(손으로 지정)
track_window = (c,r,w,h)

# set up the ROI for tracking
roi = frame[r:r+h, c:c+w]
hsv_roi =  cv.cvtColor(roi, cv.COLOR_BGR2HSV)

# low light에 의한 오류를 피하기 위해 low light 값을 제거 (h, s, v)
mask = cv.inRange(hsv_roi, np.array((0., 60.,32.)), np.array((180.,255.,255.)))

roi_hist = cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
#                      calcHist(image, channels, mask, histSize, ranges)
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
#           (src, dst, alpha, beta, type)

# Setup the termination criteria, either 10 iteration or move by atleast 1 pt
term_crit = ( cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 1 )

while(1):
    ret ,frame = cap.read()
    
    if ret == True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        
        # apply meanshift to get the new location
        ret, track_window = cv.meanShift(dst, track_window, term_crit)
        
        # Draw it on image
        x,y,w,h = track_window
        img2 = cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        cv.imshow('img2',img2)
        
        k = cv.waitKey(60) & 0xff
        if k == 27: # ESC 누르면 종료
            break
        else:
            cv.imwrite(chr(k)+".jpg",img2)
    else:
        break
    
cv.destroyAllWindows()
cap.release()