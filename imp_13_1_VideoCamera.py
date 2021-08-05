# 동영상을 카메라에서 읽고, 화면에 출력해 본다.

import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    #cv.imshow('frame',frame)
    if cv.waitKey(1) == ord('q'):
        break

# 비디오 프레임 크기, 전체 프레임수, FPS 등 출력
print('Frame width:', int(cap.get(cv.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
print('Frame count:', int(cap.get(cv.CAP_PROP_FRAME_COUNT)))

fps = cap.get(cv.CAP_PROP_FPS)
print('FPS:', fps)

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()