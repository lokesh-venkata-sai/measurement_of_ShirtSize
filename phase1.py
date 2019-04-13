#filters usage

import numpy as np
import cv2
import scipy as sp

from matplotlib import pyplot as plt

# Image operation using thresholding
img = cv2.imread('img14.jpeg')

cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("output2", cv2.WINDOW_GUI_NORMAL)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #conversion to grayscale
img1 = cv2.GaussianBlur(img,(5,5),0)
img1 = cv2.medianBlur(img1,5,5)
img1= cv2.bilateralFilter(img1,9,75,75)


cv2.imshow('output1',img)
cv2.imshow('output2',img1)
cv2.waitKey(0)