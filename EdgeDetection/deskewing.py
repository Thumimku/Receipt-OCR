import math

import cv2
import numpy as np
import matplotlib



def rotateImage(image, angle):
   (h, w) = image.shape[:2]
   center = (w / 2, h / 2)
   M = cv2.getRotationMatrix2D(center,angle,1.0)
   rotated_image = cv2.warpAffine(image, M, (w,h))
   return rotated_image


img = cv2.imread('meganew.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,300,apertureSize = 3)

# This returns an array of r and theta values
lines = cv2.HoughLines(edges, 1, np.pi / 180, 170)

skew_angle=np.array(lines.shape[0])

print(lines)



# for single_line in lines:
for r, theta in lines[0]:
   # Stores the value of cos(theta) in a
   a = np.cos(theta)

   # Stores the value of sin(theta) in b
   b = np.sin(theta)

   # x0 stores the value rcos(theta)
   x0 = a * r

   # y0 stores the value rsin(theta)
   y0 = b * r

   # x1 stores the rounded off value of (rcos(theta)-1000sin(theta))
   x1 = int(x0 + 1000 * (-b))

   # y1 stores the rounded off value of (rsin(theta)+1000cos(theta))
   y1 = int(y0 + 1000 * (a))

   # x2 stores the rounded off value of (rcos(theta)+1000sin(theta))
   x2 = int(x0 - 1000 * (-b))

   # y2 stores the rounded off value of (rsin(theta)-1000cos(theta))
   y2 = int(y0 - 1000 * (a))

   # cv2.line draws a line in img from the point(x1,y1) to (x2,y2).
   # (0,0,255) denotes the colour of the line to be
   # drawn. In this case, it is red.
   cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

   myradians = math.atan2(y1-y2, x1 - x2)
   mydegrees = math.degrees(myradians)
   if (mydegrees)<30:
      img=rotateImage(img, mydegrees)
   # img=rotateImage(img, -90)
# All the changes made in the input image are finally
# written on a new image houghlines.jpg
cv2.imwrite('linesDetectednew.jpg', img)
