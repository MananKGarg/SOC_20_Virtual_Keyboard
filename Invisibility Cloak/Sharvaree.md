# Invisibility cloak (assignment 2)
## Steps-
1. capture and store backround frame
2. Detect desired color cloth using color detection algorithm(using hsv range or trackbars)
3. Segment out desired color cloth by generating a mask.
4. Generate the final augmented output to create the magical effect of invisible cloak.
## Code-
```Python
import numpy as np                                                   #importing numpy
import cv2                                                           #importing opencv 

cap=cv2.VideoCapture(0)                                              #capturing video through webcam
fourcc=cv2.VideoWriter_fourcc(*'XVID')                               #Storing the video
out=cv2.VideoWriter('output.mp4',fourcc,20.0,(640,480))              #setting no. of frames and size

def nothing():                                                       #declaring function nothing
    pass

ret,background=cap.read()                                            #storing background frame of video

cv2.namedWindow("Tracking")                                          #Declaring window name of trackbar

cv2.createTrackbar("LH","Tracking",0,255,nothing)                    #creating trackbar of lower hue
cv2.createTrackbar('LS','Tracking',0,255,nothing)                    #creating trackbar of lower saturation
cv2.createTrackbar('LV','Tracking',0,255,nothing)                    #creating trackbar of lower value
cv2.createTrackbar('UH','Tracking',255,255,nothing)                  #creating trackbar of upper hue
cv2.createTrackbar('US','Tracking',255,255,nothing)                  #creating trackbar of upper stauration
cv2.createTrackbar('UV','Tracking',255,255,nothing)                  #creating trackbar of upper value

while(cap.isOpened()):
    ret,img=cap.read()                                               #storing each frame of the video
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                       #converting into hsv color space 

    l_h = cv2.getTrackbarPos('LH', 'Tracking')                       #
    l_s = cv2.getTrackbarPos('LS', 'Tracking')                       #getting corresponding lower value trackbars
    l_v = cv2.getTrackbarPos('LV', 'Tracking')                       #

    u_h = cv2.getTrackbarPos('UH', 'Tracking')                       #
    u_s = cv2.getTrackbarPos('US', 'Tracking')                       #getting corresponding upper value trackbars
    u_v = cv2.getTrackbarPos('UV', 'Tracking')                       #

    #l_b = np.array([25, 0, 0])                                      #array of lower bound of blue color
    #u_b = np.array([117, 255, 255])                                 #array of upper bound of blue color

    l_b = np.array([l_h, l_s, l_v])                                  #array with lower and 
    u_b = np.array([u_h, u_s, u_v])                                  #upper bounds

    if ret==True:

        mask=cv2.inRange(hsv,l_b,u_b)                                #creating mask with desired lower and upper bound values
        mask1=cv2.bitwise_not(mask)                                  #inversing mask using bitwise_not
        res=cv2.bitwise_and(img,img,mask=mask1)                      #Taking common part of original image and inverted mask
        res1=cv2.bitwise_and(background,background,mask=mask)        #Taking common part of background and mask
        res2=cv2.add(res,res1)                                       #adding both of them together to get final frame 

        out.write(res2)                                              #final output frame stored

        cv2.imshow('invisibility cloak',res2)                        #final output frame shown

        key = cv2.waitKey(1)
        if key == ord('q'):                                          #if q is pressed,exit
          break
        if key == ord('p'):                                          #if p is pressed,paused
          cv2.waitKey(-1)
            
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```
