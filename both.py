import numpy as np
import cv2
import scipy as sp

from matplotlib import pyplot as plt

# Image operation using thresholding
img = cv2.imread('img17.jpeg')

cv2.namedWindow("output", cv2.WINDOW_GUI_NORMAL)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #conversion to grayscale
img = cv2.GaussianBlur(img,(5,5),0)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imshow('image', thresh)

print("done")


kernel = np.ones((5,5),np.uint8)

#out=cv2.fastNlMeansDenoising(thresh);


closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) #closing

cv2.imwrite("otsu_Imgtest.jpeg", closing );
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel) #opening
cv2.imshow('output',opening)
#cv2.imshow('output',fill_image)
# cv2.waitKey(0)

img = cv2.imread('otsu_Imgtest.jpeg',0)
img = cv2.GaussianBlur(img,(5,5),0)
img = cv2.medianBlur(img, 5)
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
rows = cimg.shape[0]

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist=rows/8,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

print("done")
#cv2.imwrite("E:\study\sem 6\R&D\proj\impl\Hough_Img16.jpeg", cimg);
cv2.imshow('output',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()