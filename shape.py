import cv2
im1 = cv2.imread("crop_Img100-2.jpeg")
x = im1.shape
print(x)
print("width(in px): ", x[1])