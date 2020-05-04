# Invisibility Cloak

## How it works
> The code below first captures the background and store it, now whenever any blue coloured object is detected it replaces the blue part by the background at that position.

## Code
```python
import numpy as np
import cv2

cap = cv2.VideoCapture('video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')         # or give arguments as ('X','V','I','D')
out = cv2.VideoWriter('invisible_cloak.avi', fourcc, 25.0, (720,1280))

_, frame = cap.read()
while(cap.isOpened()):
    ret, img = cap.read()
    if ret == True:

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        l_l = np.array([97, 50, 25])
        u_l = np.array([155, 255, 255])
        mask1 = cv2.inRange(hsv, l_l, u_l)                              

        mask2 = cv2.bitwise_not(mask1)

        res1 = cv2.bitwise_and(frame, frame, mask=mask1)
        res2  = cv2.bitwise_and(img, img, mask=mask2)
        img = cv2.addWeighted(res1, 1, res2, 1, 0)
        out.write(img)

        cv2.imshow('Invisible_cloak', img)
        #cv2.imshow("mask1", mask1)
        #cv2.imshow("mask2", mask2)
        k = cv2.waitKey(1)
        if k == 27:
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```
