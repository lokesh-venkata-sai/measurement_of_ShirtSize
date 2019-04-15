import cv2



for x in range(1,22):
    im_name="images/from_phone/otsu/img200half-"+str(x)+".jpeg"
    image =  cv2.imread(im_name)
    #x1=image.shape[0]*1/2
    #x1=image.shape[0]*2/5
    x2=image.shape[0]
    y2=image.shape[1]
    print(image.shape[1])
    #print(x1," height= ",x2," width= ",y2)