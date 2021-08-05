# Template Matching several targets

import numpy as np
import cv2

threshold = 0.8
red = (0, 0, 255)

img = cv2.imread('images/some_game.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

tmpl = cv2.imread('images/template.jpg', cv2.IMREAD_GRAYSCALE)
w, h = tmpl.shape[:2]

res = cv2.matchTemplate(gray, tmpl, cv2.TM_CCOEFF_NORMED)

loc = np.where(res > threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), red, 3)

cv2.imshow('Results', img)
cv2.waitKey(0)
cv2.destroyAllWindows()