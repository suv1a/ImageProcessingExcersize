# 형태학적 연산자로 수평선과 수직선을 찾는다.
# from https://docs.opencv.org/master/dd/dd7/tutorial_morph_lines_detection.html

import numpy as np
import sys
import cv2 as cv

def show_wait_destroy(winname, img):
    cv.imshow(winname, img)
    cv.moveWindow(winname, 500, 0)
    cv.waitKey(0)
    cv.destroyWindow(winname)
    
# Load the image
src = cv.imread('images/music.png', cv.IMREAD_COLOR)
# Check if image is loaded fine
if src is None:
    print ('Error opening image')
    sys.exit()
    
# Show source image
cv.imshow("src", src)

# Transform source image to gray if it is not already
if len(src.shape) != 2:
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
else:
    gray = src

# Show gray image
show_wait_destroy("gray", gray)

# Apply adaptiveThreshold at the bitwise_not of gray
gray = cv.bitwise_not(gray)
bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                            cv.THRESH_BINARY, 15, -2)

# Show binary image
show_wait_destroy("binary", bw)

# Create the images that will use to extract the horizontal and vertical lines
horizontal = np.copy(bw)
vertical = np.copy(bw)

# Specify size on horizontal axis
cols = horizontal.shape[1]
horizontal_size = cols // 30    # kernel size

# Create structure element for extracting horizontal lines through morphology operations
horizontalStructure = cv.getStructuringElement(cv.MORPH_RECT, (horizontal_size, 1))

# Apply morphology operations (opening)
horizontal = cv.erode(horizontal, horizontalStructure)
horizontal = cv.dilate(horizontal, horizontalStructure)

# Show extracted horizontal lines
show_wait_destroy("horizontal", horizontal)

# Specify size on vertical axis
rows = vertical.shape[0]
verticalsize = rows // 30   # kernel size

# Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv.getStructuringElement(cv.MORPH_RECT, (1, verticalsize))

# Apply morphology operations (opening)
vertical = cv.erode(vertical, verticalStructure)
vertical = cv.dilate(vertical, verticalStructure)

# Show extracted vertical lines
show_wait_destroy("vertical", vertical)

# Inverse vertical image
vertical = cv.bitwise_not(vertical)
show_wait_destroy("vertical_bit", vertical)

'''
Extract edges and smooth image according to the logic
1. extract edges
2. dilate(edges)
3. src.copyTo(smooth)
4. blur smooth img
5. smooth.copyTo(src, edges)
'''
# Step 1
edges = cv.adaptiveThreshold(vertical, 255, cv.ADAPTIVE_THRESH_MEAN_C, \
                            cv.THRESH_BINARY, 3, -2)
show_wait_destroy("edges", edges)

# Step 2
kernel = np.ones((2, 2), np.uint8)
edges = cv.dilate(edges, kernel)
show_wait_destroy("dilate", edges)

# Step 3
smooth = np.copy(vertical)

# Step 4
smooth = cv.blur(smooth, (2, 2))

# Step 5
(rows, cols) = np.where(edges != 0)
vertical[rows, cols] = smooth[rows, cols]

# Show final result
show_wait_destroy("smooth - final", vertical)
