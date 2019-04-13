import cv2
from cv2 import CascadeClassifier as cs
img = cv2.imread('images/img75-3.jpeg')

cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)

x=cs.read(img)
