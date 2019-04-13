import cv2

class cropimage:
    def crop_bottom_half(image):
        x1=image.shape[0]/2
        x2=image.shape[0]
        y1=0
        y2=image.shape[1]
        print(x1," x2= ",x2," ",y1," ",y2)
        cropped_img = image(Rect(0, image.rows/2, image.cols, image.rows/2))
        cropped_img = image[0:640,0:960]
        return cropped_img

    im_name="images/img200-1.jpeg"
    image = cv2.imread(im_name)

    cv2.namedWindow("output1", cv2.WINDOW_GUI_NORMAL)
    print(image.shape)
    img=crop_bottom_half(image)


    cv2.imshow('output1',img)
    cv2.waitKey(0)