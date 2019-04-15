# Python program to transform an image using
# threshold.
import numpy as np
import cv2
import scipy as sp

from matplotlib import pyplot as plt

# Image operation using thresholding
img = cv2.imread('images/from_phone/img75-1.jpg')

cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("output2", cv2.WINDOW_GUI_NORMAL)

fgbg = cv2.createBackgroundSubtractorMOG2(128,cv2.THRESH_BINARY,1)
masked_image = fgbg.apply(img)
masked_image[masked_image==127]=0


cv2.imshow('output1',img)
cv2.imshow('output2',masked_image)
cv2.waitKey(0)