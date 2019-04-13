# Python program to transform an image using
# threshold.
import numpy as np
import cv2
import scipy as sp

from matplotlib import pyplot as plt

# Image operation using thresholding
img = cv2.imread('images/cropimg200-21.jpeg')
#img = cv2.imread('oldimg/image2.jpg')
cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)

#cv2.namedWindow("output2", cv2.WINDOW_GUI_NORMAL)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #conversion to grayscale
img = cv2.GaussianBlur(img,(5,5),0)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
#cv2.imshow('image', thresh)

print("done")


kernel = np.ones((5,5),np.uint8)

#out=cv2.fastNlMeansDenoising(thresh);


closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) #closing

cv2.imwrite("E:\study\sem 6\R&D\proj\impl\images\otsu_img\otsu_cropimg200-21.jpeg", closing );
#cv2.imwrite("E:\study\sem 6\R&D\proj\impl\oldimg\otsu_image2.jpeg", closing )
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel) #opening
cv2.imshow('output1',opening)

edges = cv2.Canny(img,100,200)
plt.subplot(121),plt.imshow(opening,cmap = 'binary')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'binary')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


#inv_img=cv2.bitwise_not(opening)
#cv2.imshow('output2',fill_image)
cv2.waitKey(0)
