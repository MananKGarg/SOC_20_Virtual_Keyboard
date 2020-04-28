## Invisibility cloak
```python
import numpy as np # importing required packages
import cv2

def nothing(x):
    pass

cap = cv2.VideoCapture(0) # to activate webcam

for i in range(30):          # to read the background
  r,background = cap.read()

while True:                  # to start capturing the video
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # to convert the BGR frames of captured video to HSV

    lh = 92             # the bounds to seperate the mask
    ls = 104
    lv = 100

    uh = 255
    us = 255
    uv = 255

    l_b=np.array([lh,ls,lv])   # array with the lower bounds
    u_b=np.array([uh,us,uv])   # array with the upper bounds

    mask1= cv2.inRange(hsv,l_b,u_b) # mask to seperate the cloak
    mask2 = cv2.bitwise_not(mask1)  # reverse the masked pixels

    mask2 = cv2.morphologyEx(mask2, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8)) # morphing done to get a smoother mask

    res1= cv2.bitwise_and(frame,frame,mask=mask2)                 # to get the part except the cloak
    res2 = cv2.bitwise_and(background, background, mask=mask1)    # to get the cloak with background visible

    final = cv2.add(res1, res2) # combining res1 and res2 to get final frame

    cv2.imshow('frame', frame)  # displaing everything
    cv2.imshow('mask2', mask2)
    cv2.imshow('res2', res2)
    cv2.imshow('res1', res1)
    cv2.imshow('final', final)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

