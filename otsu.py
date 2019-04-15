# Python program to transform an image using
# threshold.
import numpy as np
import cv2
import scipy as sp
from crop import cropimage
from matplotlib import pyplot as plt

# Image operation using thresholding
#img = cv2.imread('images/cropimg200-21.jpeg')
#img = cv2.imread('oldimg/img25.jpeg')

for x in range(21,22):
    im_name="images/from_phone/img200-"+str(x)+".jpg"
    #im_name="oldimg/img28.jpeg"
    img = cv2.imread(im_name)

    cropped = cropimage.crop_bottom_half(img)
    cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)
    #cv2.namedWindow("output2", cv2.WINDOW_GUI_NORMAL)
    cropped = cv2.GaussianBlur(cropped, (5, 5), 0)
    #img = cv2.GaussianBlur(img,(5,5),0)
    gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY) #conversion to grayscale
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    #cv2.imshow('image', thresh)

    print("done")


    kernel = np.ones((5,5),np.uint8)

    #out=cv2.fastNlMeansDenoising(thresh);


    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel) #closing
    im_name1 = "images/from_phone/otsu/img200fourbynine-" + str(x) + ".jpeg"


    #cv2.imwrite("E:\study\sem 6\R&D\proj\impl\images\otsu_img\otsu_cropimg200-21.jpeg", closing );
    #cv2.imwrite("E:\study\sem 6\R&D\proj\impl\oldimg\otsu_img28.jpeg", closing )
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel) #opening
    #cv2.imwrite(im_name1, opening)
    cv2.imshow('output1',opening)

    edges = cv2.Canny(img,100,200)
    plt.subplot(121),plt.imshow(opening,cmap = 'binary')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'binary')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


    #inv_img=cv2.bitwise_not(opening)
    #cv2.imshow('output2',fill_image)
    cv2.waitKey(0)
