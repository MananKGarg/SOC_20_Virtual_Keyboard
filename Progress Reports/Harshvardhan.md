Week 1-4
I went through all of the resources sent by mentor. I didn't have anything to practice then as my phone display had been damaged, and I lost contact from the group.

Week 5-7
I tried to gain access to the group, but couldn't really as my face still is continuing to face the same problem. I learned some amount of Python on my own-- it's FUN!

Week 8-9
Soon after gaining access to the Whatsapp group( I literally had to DESTROY my old whatsapp account), I tried coping up with my fellowmates, but I took up a lot of time. I did get the laptop repaired as well(the one having Windows 10;my windows 7 couldn't allow Python 3.5+ versions). I tried quiter hard to get to the actual motive of this project, just focusing on Virtual Keyboard. Just recently, I did take help from my colleagues, and they helped happily through all my doubts. I finally have done it, but my GitHub couldn't upload anything on Manan's GitHub, coz I didn't accept the invitation in time(I had no access anyways). I am quite tensed whether or not my project, though completed on-time, would be accepted. But truly, SoC is quite fun!!

Here follows my invisibility cloak program(thanks to my friends for guiding me):

import cv2
import numpy as np
cap = cv2.VideoCapture(0)
four_cc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("video.mp4", four_cc, 20.0, (640,480))

# Capturing and storing background frame

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
	
	  ub  = np.array([180,255,255])
	
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
