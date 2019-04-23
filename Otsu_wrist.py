# Python program to transform an image using
# threshold.
import numpy as np
import cv2
import scipy as sp
from crop import cropimage
from matplotlib import pyplot as plt

# Image operation using thresholding

#im_name="images/from_phone/img75-"+str(x)+".jpg"
im_name="oldimg/img32.jpeg"
img = cv2.imread(im_name)

cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)
#cv2.namedWindow("output2", cv2.WINDOW_GUI_NORMAL)

img = cv2.GaussianBlur(img,(5,5),0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)


kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) #closing

#cv2.imwrite("E:\study\sem 6\R&D\proj\impl\images\otsu_img\otsu_cropimg200-21.jpeg", closing );
#cv2.imwrite("E:\study\sem 6\R&D\proj\impl\oldimg\otsu_img28.jpeg", closing )
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel) #opening
cv2.imwrite("E:\study\sem 6\R&D\proj\impl\oldimg\otsu_img32.jpeg", opening)
cv2.imshow('output1',opening)

edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(opening,cmap = 'binary')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'binary')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

cv2.waitKey(0)
