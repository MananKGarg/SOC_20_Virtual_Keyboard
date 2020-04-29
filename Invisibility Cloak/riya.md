```python
import numpy as np 
import cv2 

cap = cv2.VideoCapture(0)                                                 # to capture video
fourcc = cv2.VideoWriter_fourcc(*'XVID')                                  # fourcc command to be given as second argument in VideoWriter function
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))              # to create an output 

ret,img = cap.read()                                                      # capturing background

def nothing(x):
	pass

cv2.namedWindow("tracking")                                               # creating a window named tracking
# creating trackbars
cv2.createTrackbar("LH", "tracking", 0, 255, nothing)	
cv2.createTrackbar("LS", "tracking", 0, 255, nothing)	
cv2.createTrackbar("LV", "tracking", 0, 255, nothing)	
cv2.createTrackbar("UH", "tracking", 255, 255, nothing)	
cv2.createTrackbar("US", "tracking", 255, 255, nothing)	
cv2.createTrackbar("UV", "tracking", 255, 255, nothing)


while(cap.isOpened()):
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                          # converting BGR frame to HSV

    # trackbar positions for lower and upper limits of hue, saturation and value
    l_h = cv2.getTrackbarPos("LH", "tracking")	
    l_s = cv2.getTrackbarPos("LS", "tracking")	
    l_v = cv2.getTrackbarPos("LV", "tracking")

    u_h = cv2.getTrackbarPos("UH", "tracking")	
    u_s = cv2.getTrackbarPos("US", "tracking")	
    u_v = cv2.getTrackbarPos("UV", "tracking")	
    
    # creating the lower and upper bounds for the color 
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    
    # creating masks and then applying bitwise opperations
    mask = cv2.inRange(hsv, l_b, u_b)
    mask1 = cv2.bitwise_not(mask)
    res = cv2.bitwise_and(frame, frame, mask=mask1)
    resb = cv2.bitwise_and(img, img, mask=mask)
    resf = cv2.add(res, resb)


    out.write(res2)

    cv2.imshow('output', resf)


    k = cv2.Waitkey(10)
    if k==27:
    	break


cap.release()
out.release()
cv2.destroyAllWindows
```
