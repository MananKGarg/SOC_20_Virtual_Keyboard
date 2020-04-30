
# Invisibility Cloak
```python
#This code was made by Paarth Jain(4/2020)

import cv2
import numpy as np 

def nothing(x):                                                #Nothing function for cv2.createTrackbar()
pass

cap = cv2.VideoCapture(0)                                      #capturing the webcam video
_,bg = cap.read()                                              #keep the first frame empty in order to store the background

fourcc = cv2.VideoWriter_fourcc(*'XVID')                       #fourcc stores the codec information
out = cv2.VideoWriter('inv_cloak.avi',fourcc,20.0, (640,480))  #specifying the output file with the relevant arguments(
                                                               #filepath, codec, frame rate, and resolution  
 


cv2.namedWindow('Tracking')                                    # Named window for trackbars
l_h = cv2.createTrackbar('LH', 'Tracking', 126, 255, nothing)
u_h = cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
l_s = cv2.createTrackbar('LS', 'Tracking', 64, 255, nothing)        #creating trackbars with initial l_hsv and u_hsv values 
                                                                    #fixed in order to make it work for a pink cloth.
u_s = cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
l_v = cv2.createTrackbar('LV', 'Tracking', 127, 255, nothing)
u_v = cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while cap.isOpened:
    ret, frame = cap.read()
    if frame is None:                                         #checking whether webcam works
        break

    cv2.imshow('Frame', frame)                                # output from webcam for comparison with original result.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)              # converting to HSV format because it is easier to manipulate
                                                              #the trackbars (hsv is intuitive and easy)
    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
                                                              #getting the values from trackbars
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b)                        # masking the original video (the cloak area pixels become 255 and others become 0)
    mask2 = cv2.bitwise_not(mask)                            # preparing another mask which is the "not" of the first one

    res1 = cv2.bitwise_and(frame, frame, mask= mask2)        # This gives the same as original video only the cloak area is black 
    res2 = cv2.bitwise_and(bg, bg, mask= mask)               #This gives a video where cloak region is replaced by the background and rest is black.

    res = cv2.bitwise_or(res1, res2)                         # Taking the "or" of the above two results gives us the desired result.
    # cv2.imshow('mask',mask)
    cv2.imshow('result', res)   
    
    out.write(res)                                           #saving the result to out 
    
    keyboard = cv2.waitKey(100)
    if keyboard == ord('q') or keyboard == 27:               # program exits by pressing 'q' or 'esc' button
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```
