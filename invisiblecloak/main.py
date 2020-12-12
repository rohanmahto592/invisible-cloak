import cv2
import numpy as np
cap=cv2.VideoCapture(0)
back=cv2.imread('image.jpg')

while cap.isOpened():
    res,img=cap.read()
    #cv2.imshow("image",img)
    #cv2.imwrite("image.jpg",img)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    # how to get hsv value
    #lower:hue-10,100,100,upper:hue+10,255,255
    red=np.uint8([[[0,0,255]]])
    hsv_red=cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
    #cv2.imshow("upper", hsv)
    #getting the hsv value of black of bgr
    #print(hsv_black)
    l_red=np.array([155,25,0])
    u_red=np.array([179,255,255])
    mask=cv2.inRange(hsv,l_red,u_red) # taking all the color that are  in range of lower nad upper red will be taken from the hsv  and mask that
    #detect all things  which are red
    mask=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    #cv2.imshow("upper", mask)
    part1=cv2.bitwise_and(back,back,mask=mask)# all the image which was hidden by the red color cloth will get change by the background color
    #cv2.imshow("upper1", part1)
    mask=cv2.bitwise_not(mask) # it will detect the background except red
    #cv2.imshow("upper", mask)

    #detect all things whic are not red
    part2=cv2.bitwise_and(img,img,mask=mask) # it will show the background.it will act as the transperancy.



    cv2.imshow("cloak",part1+part2)

    if cv2.waitKey(5)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()