# 폴더에 있는 영상을 읽고, 화면에 보인다.

import cv2

img = cv2.imread('images/Lenna.png', cv2.IMREAD_ANYCOLOR)
cv2.imshow('Image Processing', img)

cv2.waitKey(0)
cv2.destroyAllWindows()