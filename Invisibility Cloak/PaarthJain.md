
# Invisibility Cloak
```python
import cv2
import numpy as np 

def nothing(x):
pass

cap = cv2.VideoCapture(0)
_,bg = cap.read()       #keep the first frame empty in order to store the background

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('inv_cloak.avi',fourcc,20.0, (640,480))

cv2.namedWindow('Tracking')
l_h = cv2.createTrackbar('LH', 'Tracking', 126, 255, nothing)
u_h = cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
l_s = cv2.createTrackbar('LS', 'Tracking', 64, 255, nothing)
u_s = cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
l_v = cv2.createTrackbar('LV', 'Tracking', 127, 255, nothing)
u_v = cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:
    ret, frame = cap.read()
    if frame is None:
        break

    cv2.imshow('Frame', frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')

    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    mask2 = cv2.bitwise_not(mask)

    res1 = cv2.bitwise_and(frame, frame, mask= mask2)
    res2 = cv2.bitwise_and(bg, bg, mask= mask)

    res = cv2.bitwise_or(res1, res2)
    # cv2.imshow('mask',mask)
    cv2.imshow('result', res)
    out.write(res)
    keyboard = cv2.waitKey(100)
    if keyboard == ord('q') or keyboard == 27:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
```
