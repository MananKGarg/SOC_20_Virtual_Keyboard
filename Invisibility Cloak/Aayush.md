```python
import numpy as np
import cv2


def nothing():
    pass

cap = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")                          # foucc code required to save video
out=cv2.VideoWriter("outputfinal.avi",fourcc,20.0,(640,480))    # creating an video writer object
# cv2.namedWindow('Tracking')
# cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)         #
# cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)         # created trackbars to set upper bound and lower bound
# cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)         # HSV values for detection of colored cloth
# cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)       #
# cv2.createTrackbar("US", "Tracking", 255, 255, nothing)       #
# cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)       #

for i in range(30):                                             #
    _ , back = cap.read()                                       # To capture the background
    if not _:                                                   # for loop is used so that we can capture
        continue                                                # non moving object

#back = np.flip()

while cap.isOpened():
    ret, frame = cap.read()
    print(frame.shape)
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)            # Color detection works best on HSV so converting to HSV
        # l_b = cv2.getTrackbarPos("LH", "Tracking")            #
        # l_g = cv2.getTrackbarPos("LS", "Tracking")            #
        # l_r = cv2.getTrackbarPos("LV", "Tracking")            # Getting the tracker values
        #                                                       #
        # u_b = cv2.getTrackbarPos("UH", "Tracking")            #
        # u_g = cv2.getTrackbarPos("US", "Tracking")            #
        # u_r = cv2.getTrackbarPos("UV", "Tracking")            #
        #
        # low_b = np.array([l_b, l_g, l_r])                     # setting upper bound and lower bound according
        # up_b = np.array(([u_b, u_g, u_r]))                    # to tracker values
        low_b = np.array([85, 100, 0])
        up_b = np.array([134, 255, 247])

        mask1 = cv2.inRange(hsv, low_b, up_b)                   #
        mask2 = cv2.bitwise_not(mask1)                          # creating two masks one for original frame
        res1 = cv2.bitwise_and(frame, frame, mask=mask2)        # inverse mask for the background frame
        back_g = cv2.bitwise_and(back, back, mask = mask1)      #
        res2 = cv2.add(res1, back_g)                            # adding both the frame and background to get
        cv2.imshow('result', res2)                              # the final magical effect
        out.write(res2)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
