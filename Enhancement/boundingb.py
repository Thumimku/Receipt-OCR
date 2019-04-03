import cv2
import numpy as np

# read and scale down image
# wget https://bigsnarf.files.wordpress.com/2017/05/hammer.png
img = cv2.pyrDown(cv2.imread('test2.jpg', cv2.IMREAD_UNCHANGED))
# # Apply dilation and erosion to remove some noise
# kernel = np.ones((1, 1), np.uint8)
# img = cv2.dilate(img, kernel, iterations=10)
# img = cv2.erode(img, kernel, iterations=1)
#
# # Apply blur to smooth out the edges
# img = cv2.GaussianBlur(img, (5, 5), 0)
# threshold image
# ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
#                                   127, 255, cv2.THRESH_BINARY)

threshed_img = cv2.adaptiveThreshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
# find contours and get the external one

kernel = np.ones((1, 1), np.uint8)
threshed_img = cv2.dilate(threshed_img, kernel, iterations=1)
threshed_img = cv2.erode(threshed_img, kernel, iterations=1)
# img[threshed_img == 255] = 0
# img[threshed_img == 0] = 255

# threshed_img = cv2.GaussianBlur(threshed_img, (9, 9), 0)


contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


# with each contour, draw boundingRect in green
# a minAreaRect in red and
# a minEnclosingCircle in blue


for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    # draw a green rectangle to visualize the bounding rect

    if ((w*h)>80):
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(x,y,w,h)

    else:
        threshed_img[y:y+h, x:x+w]=255

    # get the min area rect
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    # convert all coordinates floating point values to int
    box = np.int0(box)
    # draw a red 'nghien' rectangle


    # cv2.drawContours(img, [box], 0, (0, 0, 255))

    # finally, get the min enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    # convert all values to int
    center = (int(x), int(y))
    radius = int(radius)
    # and draw the circle in blue


    # img = cv2.circle(img, center, radius, (255, 0, 0), 2)

print(len(contours))
# cv2.drawContours(img, contours, -1, (255, 255, 0), 1)

img[threshed_img == 0] = 0
img[threshed_img == 255] = 255
cv2.imwrite('output.jpg',img)
cv2.imshow("contours", img)
cv2.waitKey(0)

cv2.destroyAllWindows()