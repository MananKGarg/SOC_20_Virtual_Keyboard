# Paper keyboard implementation
### Steps-
1. Reading of video.
2. Masking the frame to get only the pointer visible.
3. Performing perspective transform to get the main rectangle of the keyboard.
4. Extracting the keys of the keyboard and appending it into a list.
5. Detecting whether the key is presssed or not.
6. Display the keys which are being pressed.


# Code

```
import numpy as np
import cv2
import sys

cap = cv2.VideoCapture(0)
count,flag,shift,caps = 0,1,False,True
pts1 = np.float32([[0,0],[640,0],[640,480],[0,480]])
pts2 = np.float32([[0,0],[640,0],[640,480],[0,480]])
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20,(640,480))


def mask(frame): #masks the frame and returns image which has pointers visible 
        
	h,s,v = 5,180, 23
	H,S,V = 15,255,180
	low = np.array([h,s,v]) 
	high = np.array([H,S,V]) 
	frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) 
	mask = cv2.inRange(frame,low,high) # Create a mask with low and high filters
	img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7,7),np.int8),10)
	return img

def transform(thresh,frame,pts1): #detects the corners of the the keyboard to finally crop the big rectangle
        
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

def extract(keyboard): #detects the keys and append them to a list by reading the keys at each location from a manually written text file
        
	images,location = [],[]
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
			pts1 = np.float32(a[c])
			pts2 = np.float32([[0,0],[300,0],[300,300],[0,300]])
			M = cv2.getPerspectiveTransform(pts1,pts2)
			dst = cv2.warpPerspective(keyboard,M,(300,300))
			images.append(dst.copy())
			location.append((a[c[0]],a[c[2]]))
			print('keyboard')
	images,location = zip(*sorted(zip(images,location),key = lambda x: (x[1][0][1]//40,x[1][0][0])))
	f = open('keyboard.txt')
	data = f.read().replace('\n', '')
	f.close()
        
	return (images,data,np.array(location))

def display(pressed,text,frame,typed,shift,caps): #displays the pressed keys on the frame
        
	for i in pressed:
		if(text[i]=='↲'):
			x = '\n'
		elif(text[i]=='↑'):
			x =''
			shift = not shift
		elif(shift^caps):
			x = text[i]
		else:
			x = text[i].lower()
		typed += x
		print(typed ,end = '\r')
	return (typed,shift)

while(True):

	_,frame = cap.read()
	touched = set()
	pressed = set()
	CAPS = set()
	if not count:
		h,w = frame.shape[:2]
		touched_1 = set()
		touched_2 = set()
		typed,text = '',''

	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
			 cv2.THRESH_BINARY_INV,15,15)

	pts1,contours = transform(thresh,frame,pts1)

	M = cv2.getPerspectiveTransform(pts1,pts2)
	keyboard = cv2.warpPerspective(frame,M,(640,480))
	if (pts1-pts2).any() and flag:
		t_keyboard = cv2.warpPerspective(thresh,M,(640,480))
		flag = 0
		_,board = cv2.threshold(t_keyboard, 100, 255, cv2.THRESH_BINARY_INV)
		images,text,location = extract(board)
		l = len(location)

	frame = cv2.rectangle(frame,(0,0),(640,50),(0,0,0),-1)
	frame = cv2.rectangle(frame,(0,400),(640,480),(0,0,0),-1)
	pointers = mask(keyboard)

	contours,_ = cv2.findContours(pointers,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	pointers = cv2.cvtColor(pointers,cv2.COLOR_GRAY2BGR)
	k = 0
	for c in contours: 
		x,y,w,h = cv2.boundingRect(c)
		if w*h >200:
			cv2.rectangle(pointers,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.rectangle(keyboard,(x,y),(x+w,y+h),(0,255,0),2)
			try:
				m = list(filter(lambda k : y>location[k][0][1] and y<location[k][1][1],range(l)))
				n = list(filter(lambda k: x>location[k][0][0] and x<location[k][1][0],m))

				if len(n)==1:
					touched.update(n)
					if text[n[0]].isascii():
						string = text[n[0]]
						cv2.putText(frame,string,(5+k,40),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),2)
						k += 30
			except:
				pass
	if count% 15 == 5:
		pressed = touched.intersection(touched_1)
		touched_1 = touched

	(typed,shift) = display(pressed, text, frame, typed, shift,caps)

	cv2.putText(frame,typed+'|',(0,460),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2)

	cv2.imshow('keyboard',keyboard)
	cv2.imshow('frame',frame)
	out.write(frame)
	count+=1
	if cv2.waitKey(10) == ord('q'):
		break
print('')
cv2.destroyAllWindows()
cap.release()
out.release()
```
