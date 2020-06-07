# Paper keyboard using opencv

```python
import cv2
import numpy as numpy
import time
import datetime

#capturing the video
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('paper keyboard.avi', fourcc, 20.0, (1280,720))
#creating a keyboard
keyboardnp.array(['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','.',',','/',';','','\n','<','>','?',':','"','{','}'])
keys = np.reshape(keyboard, (6,10))
print(keys)
fgbg = cv2.bgsegm.createBackgroundSubtractororMOG()

#recognising the keyboard on the page
def preprocess(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	thg = cv2.adaptiveThreshhold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 71, 7)
	gblur = cv2.GaussianBlur(thg, (5, 5), 0)
	edges = cv2.Canny(gblur, 50, 150, apertureSize=3)

	contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

	for cnt in contours:
		area = cv2.contourArea(cnt)

		if area > 4000:
			approx = cv2.approxPolyDP(cnt, 20, True)
			cv2.drawContours(img, [approx], 0, (255, 0, 0), 5)

			pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])
			screenpts = np.float32([[0, 0], [449, 0], [0, 449], [449, 449]])

			matrix = cv2.getPerspectiveTransform(pts, screenpts)
			result = cv2.warpPerspective(thg, matrix, (450, 450))

	return result

#defining which key is pressed
def key_is_pressed(old_i, old_j)
    for i in range(6):
        if i*75<=old_i and 75*(i+1)>old_i:
            for j in range(10):
                if j*45<=old_j and 45*(j+1)>old_j:
                    x, y = i, j 
                    
    for key, coords in dict_key.items():
        if (x, y)==coords: 
            return key
                
                    
def the_highest_point(c):
    highest_point = tuple(c[c[:,:,1].argmin()][0])
    return highest_point    

#checking if the key is pressed or not
def check_key(c):
    global old_i, old_j, i, j
    (old_i, old_j) = (i,j) 
    (i, j) = the_highest_point(c)    
    if (old_i, old_j) != (i,j):  
      current_time = datetime.now() 
    future_time = datetime.now()
    diff = future_time - current_time
    if diff.microseconds>= 2000000: 
        return pressed_key(old_i, old_j) 


while cap.isOpened():
    _, frame = cap.read()
    frame = preprocess(frame) 
        
    c = max(frame, key = cv2.contourArea) 

    x = check_key(c, frame)
    frame = cv2.putText(frame, ''.join(x), (30,30), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 0, 0)) 
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break 
      
cap.release()
cv2.destroyAllWindows()

```
