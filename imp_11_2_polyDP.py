# 윤곽점들을 다각형으로 근사

import cv2

src = cv2.imread("images/contourDP.jpg", cv2.IMREAD_COLOR)

gray = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

cv2.drawContours(src, contours, 0, (0, 255, 0), 3)
for contour in contours:
    epsilon = cv2.arcLength(contour, True) * 0.01
    # epsilon = cv2.arcLength(contour, True) * 0.1
    approx_poly = cv2.approxPolyDP(contour, epsilon, True)

    for approx in approx_poly:
        cv2.circle(src, tuple(approx[0]), 5, (255, 0, 0), -1)

cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyAllWindows()