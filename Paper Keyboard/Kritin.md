# PAPER KEYBOARD
### HOW TO USE-
1. Select the corner of keyboard (in the order top left,top right,bottom left,bottom right)
2. A circle will be displayed as soon as you left click to indicate selected points.
3. A new window will be opened when 4 points are selected.
4. A trackbar will also be availaible throughout to select upper and lower values for detecting mask.
5. By default trackbar values are set for orange colour.
6. A green rectangle will indicate selection of caps lock key

## CODE

```
import cv2
import numpy as np
from datetime import datetime
import time

newkey1=np.array(['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','\n','Z','X','C','V','B','N','M',' ',' ','shift',':',';','"',"'",',','.','<','>','/','?'])
cap_keys=np.reshape(newkey1,(6,10))
newkey2=np.array(['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','\n','z','x','c','v','b','n','m',' ',' ','shift',':',';','"',"'",',','.','<','>','/','?'])
small_keys=np.reshape(newkey2,(6,10))
check_caps=1


circles = np.zeros((4, 2), np.int)
counter = 0
text = ''
def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 9, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 160, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 120, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 12, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 250, 255, nothing)

def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1

cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, img = cap.read()
    if counter == 4:
        width, height = 1280, 720
        pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imgOutput = cv2.warpPerspective(img, matrix, (width, height))
        toshow = imgOutput
        #cv2.imshow("Output Image ", imgOutput)

        hsv = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2HSV)

        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")

        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")

        l_b = np.array([l_h, l_s, l_v])
        u_b = np.array([u_h, u_s, u_v])

        mask = cv2.inRange(hsv, l_b, u_b)
        M = cv2.moments(mask)
        if M["m00"] != 0:
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
        else:
            x, y = 0, 0

        #cv2.imshow('mask', mask)
        #print(x)
        if (check_caps % 2 == 0):
            toshow = cv2.rectangle(toshow, (1152, 480), (1280, 600), (0, 255, 0), 3)
        if (x!=0 or y!=0):
            i= x//128
            j= y//120
            if (i==9 and j==4):
                check_caps=check_caps+1

            else:
                if(check_caps%2!=0):
                    text = text + cap_keys[j][i]

                else:
                    text = text + small_keys[j][i]


            cv2.circle(toshow, (x, y), 3, (0, 255, 0), cv2.FILLED)
            time.sleep(1)
        cv2.putText(toshow,text,(10,30),cv2.FONT_HERSHEY_COMPLEX_SMALL,.5,(255,0,0))
        cv2.circle(toshow, (x, y), 3, (0, 255, 0), cv2.FILLED)
        cv2.imshow('toshow',toshow)


    for x in range(0, 4):
        cv2.circle(img, (circles[x][0], circles[x][1]), 3, (0, 255, 0), cv2.FILLED)


    cv2.imshow("Original Image ", img)
    print(check_caps)
    cv2.setMouseCallback("Original Image ", mousePoints)
    cv2.waitKey(100)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

```
