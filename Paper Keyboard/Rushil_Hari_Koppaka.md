# how to use
1. Run the code.
2. We have to remove our finger from the screen after everytime time we tap a button.
3. Works even if u tap the key,no necessary time stamp.
4. press 'q' to quit.
# code
```python
#Background subtraction
import cv2
import numpy as np
from datetime import datetime


keyboardL=np.array(['!','@','#','$','%','^',r'&',r'*',r'(',r')','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','\n','Z','X','C','V','B','N','M',' ',' ','shift',r':',r';',r'"',r"'",r',',r'.',r'<',r'>',r'/',r'?'])
keys=np.reshape(keyboardL,(6,10))
cap = cv2.VideoCapture('bestkeyboardwithfinger.mp4')
print(keys)
fgbg=cv2.bgsegm.createBackgroundSubtractorMOG()#history=20)

max2=[10000,10000]
t2=t1=datetime.now()
output=""
keypressed=None
xbound = np.arange(0, 1281, step=128)
ybound = np.arange(0, 721, step=120)
font=cv2.FONT_HERSHEY_COMPLEX
s=0

while (cap.isOpened()):
    r,frame=cap.read()

    if frame is None:
        break

    #getting perspective image
    pts1 = np.float32(([207, 104], [1062, 94], [0, 547], [1275, 547]))
    pts2 = np.float32(([1280, 720], [0, 720], [1280, 0], [0, 0]))
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (1280, 720))

    fgmask= fgbg.apply(result)
    fgmask=cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,np.ones((5,5),np.uint8))

    contours,_=cv2.findContours(fgmask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour)<1000:
            continue
        else:
            a=np.array(contour[:, 0])#array of all points in contour
            y=list(a[:, 1])             #list of y coordinates
            top=(a[y.index(min(y)),:])#gives element with max y coordinate

            if top[1]<max2[1]:
                max2=top
                t1=datetime.now()
            else:
                t2=datetime.now()
    if len(contours) == 0:
        if (t2 - t1).total_seconds() >= 0.01:                              #can be used to shorten tie periods but we have to remove finger for this
            fgmask = cv2.circle(fgmask, tuple(max2), 50, (255, 255, 255), 3)
            result= cv2.circle(result, tuple(max2), 50, (255, 255, 255), 3)

            i = 0
            xindex = yindex = -1
            while (i <=9):

                if xbound[i] < int(max2[0]) and int(max2[0])<= xbound[i + 1]:
                    xindex = i
                if i<=5:
                    if ybound[i] < int(max2[1]) and int(max2[1])  <= ybound[i + 1]:
                        yindex = i
                i = i + 1
                if xindex != -1 and yindex != -1:
                    keypressed = keys[yindex][xindex]
                    break
            if max2[0] != 10000 and max2[1] !=0:
                if keypressed is not None:
                    print(keypressed ,end='')
                    if keypressed=='shift':
                        s=s+1
                        max2 = [10000, 10000]
                        continue

                    if s%2==0:
                        output=output+keypressed                #for capslock
                    else:
                        output=output + keypressed.lower()

        max2 = [10000, 10000]

    frame=cv2.putText(frame,output,(200,600),font,2,(0,0,0),thickness=3)
    if s%2==0:
        frame=cv2.circle(frame,(242,206),4,(0,255,0),-1)
    cv2.imshow('res',result)
    cv2.imshow('f',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
```
