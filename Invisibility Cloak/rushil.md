```
import cv2
import numpy as np

cap = cv2.VideoCapture(0)                                         #capturing video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

background_image= cv2.imread('background image.jpg')  

while (cap.isOpened()):

    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    #coverting frame to hsv format

        L=np.array([80,144,0])                     #lowerblue(hsv)
        U=np.array([125,255,172])                  #upperblue(hsv)

        mask=cv2.inRange(hsv,L,U)                 #mask of region containing blue colour

        kernel= np.ones((5,5),np.uint8)
        mask3=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel,iterations=1)   #performing opening

        frame1=frame.copy()
        frame2=background_image.copy()

        frame1[np.where(mask3==255)]=0    #converting areas in our camera video input ,where mask is true(white{255}), to black(0)
        frame2[np.where(mask3==0)]=0      #converting areas on background image, where mask is false(black{0}), to black(0)

        res= cv2.add(frame1,frame2)       #adding the two images(black parts get filled by each others parts)

        res2= cv2.medianBlur(res,5)         #for noise reduction
        res2= cv2.GaussianBlur(res2,(5,5),0)
        res2= cv2.medianBlur(res,7)

        cv2.imshow('invisibility cloak', res2)    #output
        #cv2.imshow('mask',mask3)

        out.write(res2)

        if cv2.waitKey(1) & 0xFF == ord('q'):         #press q to escape program
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```
