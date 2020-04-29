  ```python
  
  import cv2
import numpy as np
def nothing(x):
   pass
cap= cv2.VideoCapture(0)                                                         # creating an instance of VideoCapture class
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640,480))                       # to save video
ret, background = cap.read()                                                     # to get background frame
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking", 0, 255, nothing)                             # trackbar for lower hue
cv2.createTrackbar("LS","Tracking", 0, 255, nothing)                             # trackbar for lower saturation
cv2.createTrackbar("LV","Tracking", 0, 255, nothing)                             # trackbar for lower value
cv2.createTrackbar("UH","Tracking", 255, 255, nothing)                           # trackbar for Upper hue
cv2.createTrackbar("US","Tracking", 255, 255, nothing)                           # trackbar for Upper saturation
cv2.createTrackbar("UV","Tracking", 255, 255, nothing)                           # trackbar for Upper value
while(cap.isOpened()):
    ret, frame= cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("LH", "Tracking")                                 #
    l_s = cv2.getTrackbarPos("LS", "Tracking")                                 #
    l_v = cv2.getTrackbarPos("LV", "Tracking")                                 #
    u_h = cv2.getTrackbarPos("UH", "Tracking")                                 # to get current value of trackbar
    u_s = cv2.getTrackbarPos("US", "Tracking")                                 #
    u_v = cv2.getTrackbarPos("UV", "Tracking")                                 #

    l_b = np.array([l_h, l_s, l_v])                                            # lower bound value
    u_b = np.array([u_h, u_s, u_v])                                            # upper bound value
    mask = cv2.inRange(hsv, l_b, u_b)                                          # mask for red portion
    mask1 = cv2.bitwise_not(mask)                                              # mask for non-red portion
    res1 = cv2.bitwise_and(frame, frame, mask=mask)                            # shows only red portion, remaining portion is black
    res2 = cv2.bitwise_and(frame, frame, mask=mask1)                           # shows only non-red portion, remaining portion is black
    res3 = cv2.bitwise_and(background, background, mask= mask)                 # shows background in place of red portion, remaining portion is black
    final_image = cv2.add(res2, res3)                                          # shows frame with background in place of red portion
    cv2.imshow("res1", res1)
    cv2.imshow("res2", res2)
    cv2.imshow("res3", res3)
    cv2.imshow("final", final_image)                                           # final image with magical effect

    out.write(frame)                                                            # writes frame into file output.avi
    key = cv2.waitKey(1)
    if key == 27:                                                               # key pressed is escape key
        break
out.release()
cap.release()
cv2.destroyAllWindows()
```
