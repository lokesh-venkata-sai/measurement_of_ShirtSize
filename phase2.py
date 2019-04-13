import numpy as np
import cv2
import scipy as sp

from matplotlib import pyplot as plt

# Image operation using thresholding
img = cv2.imread('img5.jpeg')
cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("output2", cv2.WINDOW_GUI_NORMAL)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #conversion to grayscale
img = cv2.GaussianBlur(img,(5,5),0)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
cv2.imshow('output1', thresh)



print("done")


kernel = np.ones((5,5),np.uint8)

#out=cv2.fastNlMeansDenoising(thresh);


closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel) #opening




cv2.imshow('output2',opening)
#cv2.imshow('output',fill_image)
cv2.waitKey(0)