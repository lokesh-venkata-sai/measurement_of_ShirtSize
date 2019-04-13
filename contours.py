# python extreme_points.py
# import the necessary packages
import imutils
import cv2
from scipy.spatial import distance as dist
import numpy as np
#from crop import cropimage
x=21;
# load the image, convert it to grayscale, and blur it slightly

#print(x)

#im_name="images/cropimg75-"+str(x)+".jpeg"

im_name="oldimg\otsu_image1.jpeg"   #should give the  inversted otsu output to findContours

image = cv2.imread(im_name)
image = cv2.bitwise_not(image)
#image=cropimage.crop_bottom_half(image)
#Testing
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
#gray = cv2.Canny(gray, 100, 200)
ret3,gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
# threshold the image, then perform a series of erosions +
# dilations to remove any small regions of noise
thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.erode(thresh, None, iterations=2)
thresh = cv2.dilate(thresh, None, iterations=2)

# find contours in thresholded image, then grab the largest
# one
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

# determine the most extreme points along the contour
extLeft = tuple(c[c[:, :, 0].argmin()][0])  #red
extRight = tuple(c[c[:, :, 0].argmax()][0])   #green
extTop = tuple(c[c[:, :, 1].argmin()][0])   #blue
extBot = tuple(c[c[:, :, 1].argmax()][0])   #teal
print("exLeft: ",extLeft)
print("exRight: ",extRight)
print("exTop: ",extTop)
print("exBot: ",extBot)

print(c[:, 0, 0].argmax())
print(c[:,0,0].argmin())
print(c[[c[0].argmax()][0]])
xSorted = c[np.argsort(c[:, 0]), :]

# grab the left-most and right-most points from the sorted
# x-roodinate points
leftMost = xSorted[:2, :]
# now, sort the left-most coordinates according to their
# y-coordinates so we can grab the top-left and bottom-left
# points, respectively
leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
(tl, bl) = leftMost


#dB1 = dist.euclidean((extLeft[0], extRight[0]), (extLeft[1], extRight[1]))
#print("left: ",extLeft," right: ",extRight)
dB = dist.euclidean(extLeft,extRight)
#dB = dist.euclidean(extLeft,extBot)
#print(dB," ",dB1)
print(dB)
cv2.putText(image, "{:.1f}in".format(dB),
         (10,500), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

# draw the outline of the object, then draw each of the
# extreme points, where the left-most is red, right-most
# is green, top-most is blue, and bottom-most is teal
cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
cv2.circle(image, extLeft, 6, (0, 0, 255), -1)
cv2.circle(image, extRight, 6, (0, 255, 0), -1)
cv2.circle(image, extTop, 6, (255, 0, 0), -1)
cv2.circle(image, extBot, 6, (255, 255, 0), -1)


# show the output image
cv2.namedWindow('Image',cv2.WINDOW_NORMAL )
cv2.imshow("Image", image)
cv2.waitKey(0)