## README
Load the hsv values of pointer into hsv_values.txt else the program uses an approximation of fingernail which may not work.  
Make sure the entire keyboard is in view.  
If the key detection doesn't work properly in new lighting conditions, redefine the hsv values.  
**REQUIRES** keyboard layout as a text file in the directory.  
Download QWERTY Keyboard layout from [here](https://github.com/Sudhansh6/Virtual-Keyboard/blob/master/Final%20Code/keyboard3.txt)
Keep checking [this](https://github.com/Sudhansh6/Virtual-Keyboard/blob/master/Final%20Code/vk_build.py) for updated version

# CODE  
``` python
import cv2
import numpy as np

cap = cv2.VideoCapture(-2)
count, flag, typed, text, caps = 0,1,'','',True
pts1 = pts2 = np.float32([[0,0],[640,0],[640,480],[0,480]])
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_build.avi',fourcc,20,(640,480))
font = cv2.FONT_HERSHEY_SIMPLEX

def mask(frame):
	try:
		f = open('hsv_values.txt','r') # check if hsv values are present
		h,s,v,H,S,V = list(int(x.replace('\n','')) for x in f)
		f.close()
	except:
		h,s,v = 108, 61, 23
		H,S,V = 255,180,180

	low, high = np.array([h,s,v]), np.array([H,S,V])
	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 
	mask = cv2.inRange(frame,low,high) # Create a mask with low and high filters
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7,7),np.int8),10)
	return opening

def crop(thresh,pts1):
	contours,_ = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	cnts = sorted(contours, key=lambda x: cv2.contourArea(x),reverse = True)[0]
	a = cv2.approxPolyDP(cnts,0.01*cv2.arcLength(cnts,True),True)
	if(len(a)==4):
		a = a.reshape(-1,2)
		c = np.argsort(np.sum(a,axis = 1))
		if(a[c[1]][0] < a[c[2]][0]):
			c[2],c[1] = c[1],c[2]
		c[2],c[3]=c[3],c[2]
		pts1 = np.float32(a[c])	
	return (pts1,contours)

def extract(keyboard):
	print("Extracting keys from keyboard")
	location = []
	kcontours,_ = cv2.findContours(keyboard,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	for cnt in kcontours:
		cnt_len = cv2.arcLength(cnt, True)
		cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
		if len(cnt) == 4 and 15000>cv2.contourArea(cnt) and cv2.contourArea(cnt)> 400 and cv2.isContourConvex(cnt):
			a = cnt.reshape(-1, 2)
			c = np.argsort(np.sum(a,axis = 1))
			if(a[c[1]][0] < a[c[2]][0]):
				c[2],c[1] = c[1],c[2]
			c[2],c[3]=c[3],c[2]
			location.append((a[c[0]],a[c[2]]))
	print('Extracted')
	location = sorted(location,key = lambda x: (x[0][1]//40,x[0][0]))
	f = open('keyboard3.txt')
	data = f.read().replace('\n', '')
	f.close()

	return dict(zip(data,location))

def display(pressed,frame,caps,typed):
	x = ''
	shift = False
	if '↑' not in list(pressed):
		pass
	elif(len(pressed)==1):
		caps = not caps
		return typed,caps
	else:
		shift = True
	for i in pressed:
		if(i =='←'): 
			typed = typed[:-1]
		elif(i =='↲'):
			x = '\n'
		elif(i == '↑'):
			pass
		elif(caps^shift):
			x = i
		else:
			x = i.lower()	
		typed += x
		# print(typed ,end = '\r')
	cv2.putText(frame,typed+'|',(0,460),font,2,(255,255,255),3)
	state = 'CAPSLOCK ON' if caps else 'CAPSLOCK OFF'
	cv2.putText(frame,state,(400,30),font,1,(0,0,255),2)
	return typed,caps

while(True):
	_,frame = cap.read()
	touched, pressed = set(),set()
	if not count:
		h,w = frame.shape[:2]
		touched_1 = set()


	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
			 cv2.THRESH_BINARY_INV,15,15)

	pts1,contours = crop(thresh,pts1)

	M = cv2.getPerspectiveTransform(pts1,pts2)
	keyboard = cv2.warpPerspective(frame,M,(640,480))
	if (pts1-pts2).any() and flag:
		t_keyboard = cv2.warpPerspective(thresh,M,(640,480))
		flag = 0
		_,board = cv2.threshold(t_keyboard, 100, 255, cv2.THRESH_BINARY_INV)
		location = extract(board)
		l = len(location)

	frame = cv2.rectangle(frame,(0,0),(640,50),(0,0,0),-1)
	frame = cv2.rectangle(frame,(0,400),(640,480),(0,0,0),-1)
	pointers = mask(keyboard)

	contours,_ = cv2.findContours(pointers,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	pointers = cv2.cvtColor(pointers,cv2.COLOR_GRAY2BGR)
	i = 0
	for c in contours: 
		x,y,w,h = cv2.boundingRect(c)
		if w*h >200:
			cv2.rectangle(pointers,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.rectangle(keyboard,(x,y),(x+w,y+h),(0,255,0),2)
			m = list(filter(lambda i : y>location[i][0][1] and y<location[i][1][1],location))
			n = list(filter(lambda i: x>location[i][0][0] and x<location[i][1][0],m))

			if len(n)==1:
				touched.update(n)
				if n[0].isascii():
					cv2.putText(frame,n[0],(5+i,40),font,1.5,(255,255,255),3)
					i += 30

	if count% 15 == 5:
		pressed = touched.intersection(touched_1)
		touched_1 = touched
	(typed,caps) = display(pressed, frame, caps, typed)
	
	cv2.imshow('keyboard',keyboard)
	cv2.imshow('frame',frame)
	out.write(frame)
	count+=1
	if cv2.waitKey(10) == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
out.release()
```
