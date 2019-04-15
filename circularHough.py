import cv2
import numpy as np

img = cv2.imread('oldimg/otsu_img28.jpeg',0)
img = cv2.GaussianBlur(img,(5,5),0)
img = cv2.medianBlur(img, 5)
cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("output2", cv2.WINDOW_GUI_NORMAL)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(cimg.shape)#rows,columns,channels
rows = cimg.shape[0]

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist=rows/8,param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


print(circles) #[x,y,r]
print("done")
#cv2.imwrite("E:\study\sem 6\R&D\proj\impl\oldimg\Hough1_img27.jpeg", cimg);
cv2.imshow('output1',img)
cv2.imshow('output2',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

#radius=69 for img27, radius=70 for img28