### Code:
```python
import cv2
import numpy as np

def f(x):
    pass

# fourcc = cv2.VideoWriter_fourcc(*'XVID') 
# out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640,480))
vid = cv2.VideoCapture(0)
cv2.namedWindow('result')
_, frame0 = vid.read()                                                  #frame0 = initial background
                                                   
lb = np.array([0,0,0])                                                  #HSV lower bound
ub = np.array([255,255,255])                                            #HSV Upper bound


def click_work(event, x, y, flags, param):
    """
    Right_click=>visible
    left_click=>invisible
    """
    global lb,ub
    if event==cv2.EVENT_LBUTTONDOWN:                               
        lb[:] = [88,44,0]                                               #HSV lb color of your cloak
        ub[:] = [125,255,255]                                           #HSV ub color of your cloak
    if event==cv2.EVENT_RBUTTONDOWN:                             
        lb = np.array([0,0,0])
        ub = np.array([0,0,0])
        
        
cv2.setMouseCallback('result', click_work)                              #setting callback function

while True:
    if cv2.waitKey(1)==ord('q'):                                        #stop condition
        break
    _, frame = vid.read()
    frame1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)                     #frame in HSV form
    mask1 = cv2.inRange(frame1, lb, ub)                                 #mask of cloth  
    mask2 = np.ones_like(mask1)*255
    mask2 = cv2.bitwise_xor(mask2, mask1)                               #inverse of mask1
    frame2 = cv2.bitwise_and(frame0, frame0, mask=mask1)                #cloth background
    frame3 = cv2.bitwise_and(frame, frame, mask=mask2)                  #present frame background
    merged = cv2.add(frame2, frame3)                                    #final output

    cv2.imshow('result', merged)
    cv2.imshow('mask', mask1)
    #out.write(merged)
        
vid.release()
out.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)
```
