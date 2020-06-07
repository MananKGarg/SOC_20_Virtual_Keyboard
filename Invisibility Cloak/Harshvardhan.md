import cv2
import numpy as np
cap = cv2.VideoCapture(0)
four_cc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("video.mp4", four_cc, 20.0, (640,480))

# Capturing and storing the background frame
for i in range(60):
  ret,background = cap.read()
	
while(cap.isOpened()):
	ret, img = cap.read()
	if not ret:
    break
	# Converting the color space from BGR to HSV
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  # Generating mask to detect pink
  lb = np.array([0,120,20])
  ub = np.array([6,255,255])
  mask1 = cv2.inRange(hsv,lb,ub)
  lb = np.array([172,120,20])
	ub = np.array([180,255,255])
	mask2 = cv2.inRange(hsv,lb,ub)
	mask1 = mask1+mask2
	
  # Refining the mask corresponding to the detected color
	mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3),np.uint8),iterations=2)
	mask1 = cv2.dilate(mask1,np.ones((3,3),np.uint8),iterations = 1)
	mask2 = cv2.bitwise_not(mask1)
	# Generating the final 
	res1 = cv2.bitwise_and(background,background,mask=mask1)
  res2 = cv2.bitwise_and(img,img,mask=mask2)
  res = cv2.addWeighted(res1,1,res2,1,0)

	cv2.imshow('Invisibility cloak',res)
	
	out.write(res)
	
	if cv2.waitKey(10)==27:
	
		break

# Close the window / Release webcam 
cap.release() 
# After we release our webcam, we also release the output 
out.release()
# Destroying any associated memory usage 
cv2.destroyAllWindows()
