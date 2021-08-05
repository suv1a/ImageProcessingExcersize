# 동영상을 파일에서 읽고, 영상처리 후 출력

import numpy as np
import cv2 as cv
cap = cv.VideoCapture('images/vtest.avi')
while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    cv.imshow('frame', binary)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()