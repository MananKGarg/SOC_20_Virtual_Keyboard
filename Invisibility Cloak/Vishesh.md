#Code for invisibility cloak
```python
import numpy as np
import cv2
import time
cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('inv_out.avi', fourcc, 25.0, (720, 1280))
time.sleep(5)
background = 0  # capturing background
for i in range(50):
    ret, background = cap.read()  # capturing image
while (cap.isOpened()):
    ret, img = cap.read()

    if not ret:
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    red_lower = np.array([0, 120, 70])
    red_upper = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, red_lower, red_upper)
    red_lower = np.array([170, 120, 70])
    red_upper = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, red_lower, red_upper)
    mask1 = mask1 + mask2
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask2 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    cv2.imshow('Final Output', final_output)
    out.write(final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```
