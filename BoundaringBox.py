import cv2
import numpy as np


# Read image
im = cv2.imread("images/cropimg200-6.jpeg")

# Select ROI
r = cv2.selectROI(im)
#fromCenter = False
#r = cv2.selectROI(im, fromCenter)
print("width(in px)",im.shape[1])
# Crop image
imCrop = im[int(r[1]):int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

cv2.imwrite("E:\study\sem 6\R&D\proj\impl\Testing.jpeg", imCrop);

print("cropped width(in px) ",imCrop.shape[1])
# Display cropped image
cv2.imshow("Image", imCrop)

cv2.waitKey(0)