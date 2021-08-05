# Unsharpening에 의한 sharpening

import cv2
import sys
import numpy as np

#img = cv2.imread('images/Lenna.png', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('images/Lenna.png', cv2.IMREAD_COLOR)

if img is None:
    print('영상 읽기 실패')
    sys.exit()
    
blr = cv2.GaussianBlur(img, (0,0), 2)
result = np.clip(2.0 * img - blr, 0, 255).astype(np.uint8)

cv2.imshow('Original', img)
cv2.imshow('Result', result)
cv2.waitKey()
cv2.destroyAllWindows()