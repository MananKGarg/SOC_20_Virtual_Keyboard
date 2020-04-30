
# Mini Project - Invisibility Cloak
## Goal
The goal is to delve into the world of magic xD. On a serious note, we basically play around with openCV Library and try to mimic the invisibility cloak of Harry Potter.

## Requisites
#### Advanced Concepts - 
* What is magic!!?? xD
#### Concepts/Functions
* **[Video Capture and Video Writing](https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html)**
* **[Colour Space Transformation](https://www.geeksforgeeks.org/color-spaces-in-opencv-python/)**
* **[Bitwise Operations](https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html)**
* **[Masking](https://docs.opencv.org/3.4/d7/d37/tutorial_mat_mask_operations.html)**
* **[Trackbar](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/SoC_OpenCV-master/12.%20(Nirmal)How%20to%20Bind%20Trackbar%20To%20OpenCV%20Windows.md) (refer to the given link)**

## Plan

We store the background before hand as an image so that we can blend our captured image with it to produce invisibility effects.
Basically, what we do is that , we display the captured image other than the part occupied by the cloak.
For that part, we merge the pixels from the background image to the capured image and then display it. And that is really the secret of our invisibility cloak.
We have simply played a small trick that we stored the background already. **So beware and don't make a fool out of yourself when showing it off. Remember to store the background. xD**

Steps Employed -  
* Capture and store the background image.
* Detect the cloth by adjusting the thresholds using the trackbars (Color Detection Algorithm)
* Segment out that part of the image.
* Create the final image using the modified frame and the background image.


## Code

```python 
import cv2 as cv 
import numpy as np 

def nothing(x):							# Dummy Function as a call back for the trackbars				
	pass							# Don't do anything inside the function

fourcc = cv.VideoWriter_fourcc(*'XVID')                   	# Specifies the type of video file (in this case MPEG4)       
out = cv.VideoWriter('output.avi', fourcc, 10, (640,480))	# The output video file at 10 frames per second 

cv.namedWindow('detect')					# Creates a named window
cv.createTrackbar('LH', 'detect', 0, 255, nothing)		# Creates trackbar for Lower Hue
cv.createTrackbar('UH', 'detect', 255, 255, nothing)		# Creates trackbar for Upper Hue
cv.createTrackbar('LS', 'detect', 0, 255, nothing)		# Creates trackbar for Lower Saturation
cv.createTrackbar('US', 'detect', 255, 255, nothing)		# Creates trackbar for Upper Saturation
cv.createTrackbar('LV', 'detect', 0, 255, nothing)		# Creates trackbar for Lower Value
cv.createTrackbar('UV', 'detect', 255, 255, nothing)		# Creates trackbar for Lower Value

cap = cv.VideoCapture(0)					# Captures video using default webcam

while(cap.isOpened()):						# While the camera returns frames
	ret, frame = cap.read()					# Reading the frames
	back = cv.imread('backgound.png')			# Read the background image

	hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)		# Transform image to the HSV Color Space

	l_h = cv.getTrackbarPos('LH', 'detect')			# Obtain the Lower Hue
	l_s = cv.getTrackbarPos('LS', 'detect')			# Obtain the Upper Hue
	l_v = cv.getTrackbarPos('LV', 'detect')			# Obtain the Lower Saturation

	u_h = cv.getTrackbarPos('UH', 'detect')			# Obtain the Upper Saturation
	u_s = cv.getTrackbarPos('US', 'detect')			# Obtain the Lower Value
	u_v = cv.getTrackbarPos('UV', 'detect')			# Obtain the Upper Value

	l_b = np.array([l_h, l_s, l_v])				# Applying the lower threshsold
	u_b = np.array([u_h, u_s, u_v])				# Applying the upper threshold

	mask = cv.inRange(frame, l_b, u_b)			# Obtaining the mask
	res1 = cv.bitwise_and(back, back, mask = mask)		# Obtaining the segmented background
	inv = cv.bitwise_not(mask)				# Inverse of the mask for the frame captured
	res2 = cv.bitwise_and(frame, frame, mask = inv)		# Obtaining the segmented frame
	final = cv.bitwise_or(res1, res2)			# Obtaining the final combined image
	out.write(final)					# Writing the frame to the output video file
	cv.imshow('final', final)				# Displaying the processed image
	cv.imshow('mask', mask)					# Display the mask
	cv.imshow('detect', frame)				# Display the captured image
	k = cv.waitKey(1)					# Wait for the user to press some key
	if k == 27:						# Break if the 'ESC' key is pressed
		break

cap.release()							# Release the video variable
out.release()							# Release the output video variable
cv.destroyAllWindows()						# Close all windows forcefully
```
## References

* **[Invisibility Cloak](https://www.geeksforgeeks.org/invisible-cloak-using-opencv-python-project/)** (not required really)

