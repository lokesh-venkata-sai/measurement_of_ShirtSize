import cv2

class cropimage:
    def crop_bottom_half(image):
        #image =  cv2.imread("images/from_phone/img75-1.jpg")
        #x1=image.shape[0]*1/2
        x1=image.shape[0]*4/9
        x2=image.shape[0]
        y2=image.shape[1]
        #print(x1," height= ",x2," width= ",y2)
        #cropped_img = image(Rect(0, image.rows/2, image.cols, image.rows/2))
        cropped_img = image[0:int(x1),0:int(y2)]
        #print("cropped_img")
        #print("height=",cropped_img.shape[0]," width=",cropped_img.shape[1])
        return cropped_img


