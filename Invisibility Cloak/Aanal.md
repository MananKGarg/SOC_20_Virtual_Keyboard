The below code is for invisibility cloak. The required files/modules were opencv and numpy.
```python
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

time.sleep(1)
ret, img = cap.read()

while(cap.isOpened()):
	ret, frame = cap.read()

	if not ret:
		break

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	lb = np.array([0, 50, 50 ])
	ub = np.array([10, 255, 255])
	mask1 = cv2.inRange(hsv, lb, ub) 

	lb = np.array([170, 50, 50 ])
	ub = np.array([180, 255, 255])  
	mask2 = cv2.inRange(hsv, lb, ub)  #Red has two ranges hence we make two masks 

	mask = mask1 + mask2 #add both masks for overall mask
    
	red_image = cv2.bitwise_and(frame, frame, mask = mask) #red part segmented

	final_image = frame - red_image #to obtain non-red part in frame	

	x =cv2.add(final_image, img, mask=mask)	#red part to be covered by back ground image
	mask_inv = cv2.bitwise_not(mask)	#inverse of red-mask

	y= cv2.add(x, final_image, mask = mask_inv) #non-red part
	result = cv2.bitwise_or(x, y)	#add both for final effect.

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('result', result) #the final frame with effect.
	cv2.imshow('x', x)
	cv2.imshow('y', y)

	k=cv2.waitKey(1)
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()

 
