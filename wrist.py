import imutils
import cv2
from scipy.spatial import distance as dist
import numpy as np
from matplotlib import pyplot as plt

# from crop import cropimage
x = 1;
largest_area = 0;
largest_contour_index = 0
# load the image, convert it to grayscale, and blur it slightly
for x in range(21, 22):
    #im_name = "oldimg/otsu_image1.jpeg"
    im_name="oldimg/Hough1_img28.jpeg"
    image = cv2.imread(im_name)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret3, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cnts, hierarchy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = [cv2.contourArea(c) for c in cnts]
    max_index = np.argmax(areas)
    cnt = cnts[max_index]
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        #print(cX)
    else:
        cX, cY = 0, 0
    c = max(cnts, key=cv2.contourArea)

    height, width = image.shape[:2]
    extBot = tuple(c[c[:, :, 1].argmax()][0])  # teal
    #print(extBot[1])
    dB = dist.euclidean(extBot, (cX, height)) * 2

    print(dB)
    cv2.putText(image, "{:.1f}in".format(dB),
                (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

    cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
    cv2.circle(image, extBot, 16, (255, 0, 0), -1)
    cv2.circle(image, (cX, height), 16, (255, 255, 0), -1)

    # show the output image
    cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", image)
    cv2.waitKey(0)