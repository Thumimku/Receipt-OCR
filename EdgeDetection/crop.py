import math

import cv2
import numpy as np
import matplotlib


img = cv2.imread('linesDetectednew.jpg')
(h, w) = img.shape[:2]
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100, 300, apertureSize = 3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 170)
xw=True
wx=True
yh=True
hy=True
lines_array=np.zeros(shape=(lines.shape[0], 6))
iter=0
for single_line in lines:
   for r, theta in single_line:
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


      lines_array[iter]=[x0, x1, x2, y0, y1, y2]
      iter=iter+1






print (lines_array)
border=[0,0,0,0]

for line in lines_array:
   x0,x1,x2,y0,y1,y2=line[0],line[1],line[2],line[3],line[4],line[5]
   if (abs(y1-y2)>abs(x1-x2)):
      if((x0>w/2) and (xw)):
         border[0]=int(x0)
         xw=False


      elif(wx) and (x0<=w/2):
         border[1]=int(x0)
         wx=False


   else:
      if((y0>h/2) and (yh)):
         border[2]=int(y0)
         yh=False

      elif (hy) and (y0<=h/2):
         border[3]=int(y0)
         hy=False

img=img[border[3]:border[2], border[1]:border[0]]
# img=img[border[3]:h, 0:w]

cv2.imwrite('linesDetected2_tested_new.jpg', img)
