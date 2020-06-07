# Useful Instructions
1. This code requires you to use one finger at once for typing
2. Press the alphabet 'q' to exit the code
# Code
```python


import cv2
import numpy as np
import math
from datetime import datetime

cap = cv2.VideoCapture(0)
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT))
print(frame_height)
print(frame_width)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))
upper_key_list=np.array(['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','\n','Z','X','C','V','B','N','M',' ',' ','shift',':',';','"',"'",',','.','<','>','/','?'])
lower_key_list=np.array(['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','\n','z','x','c','v','b','n','m',' ',' ','shift',':',';','"',"'",',','.','<','>','/','?'])
upper_keys=np.reshape(upper_key_list,(6,10))
lower_keys=np.reshape(lower_key_list,(6,10))
text=" "
ret, frame1 = cap.read()
ret, frame2 = cap.read()
print(frame1.shape)
caps=False
t_1=datetime.now()
t_2=datetime.now()
y_min = 720
x_min =1280
y_store=720
x_store=1280
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    finger_tip=[x_min,y_min]
    count=0;
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) > 2000:
            count=count+1
            tip=[x,y]
            if count==1:
                y_min=y
                x_min = x
                finger_tip = [y_min, x_min]
            if(y<y_min):
                y_min=y
                x_min=x
                finger_tip=[y_min,x_min]
        if cv2.contourArea(contour) < 2000 or cv2.contourArea(contour)>50000:
            continue
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    print(finger_tip)
    if count == 0:
        t_2=datetime.now()
        #if (t_2-t_1).total_seconds()>=0.01:
        slot_x=math.floor(x_min/64)
        slot_y=math.floor(y_min/80)
        if slot_x==10 and slot_y==5:
            caps= not caps
        print(caps)
        if caps==True:
            print("upper")
            text = text+ (upper_keys[slot_x,slot_y])
        elif caps==False:
            print("lower")
            text = text + (lower_keys[slot_x, slot_y])

    else :
        t_1 = datetime.now()
        t_2 = datetime.now()


    print(text)
    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()
```

