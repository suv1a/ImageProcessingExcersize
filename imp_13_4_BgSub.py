# 동영상 배경 제거

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('images/vtest.avi')
fgbg = cv.createBackgroundSubtractorMOG2()
kernel = cv.getStructuringElement(cv.MORPH_RECT, (3,3))

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    fgmask = fgbg.apply(frame)
    fgmask = cv.morphologyEx(fgmask, cv.MORPH_OPEN, kernel) # noise 제거
    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff  # ESC로 종료
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()