## Paper Keyboard
We have made this keyboard following a series of steps:
1)Take the frame
2) Edit the frame to get only the keyboard (assuming that contour has maximum area).
3) Now start recording.
4) For each frame process it, and find difference between that frame and orginial keyboard.
5) Find the top most point of contour of this difference
6) Conforming whether key is pressed.
```python
import numpy as np
import cv2
import time

def preprocess(img):
    img = cv2.resize(img, (450, 450))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting to grayscale
    
    img_guass = cv2.GaussianBlur(img_gray, (5,5), 0) #applying guass blur

    img_thresh = cv2.adaptiveThreshold(img_guass, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 201, 5) #apply adaptive thresholding
    
    img_contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in img_contours:
        area = cv2.contourArea(cnt)
        if area>30000:  #this condition might be too high but I required that on the image I used
            
            approx = cv2.approxPolyDP(cnt, 20, True)
            cv2.drawContours(img, [approx], 0, (255, 0, 0), 5)
            pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])
            screen = np.float32([[0,0],[449, 0], [0,449], [449, 449],])
            
            matrix = cv2.getPerspectiveTransform(pts, screen)
            result = cv2.warpPerspective(img, matrix, (img.shape[0], img.shape[1]))
    (rows, cols) = result.shape[:2] 
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
    result = cv2.warpAffine(result, M, (cols, rows)) 
    
    return img

def check_key(extTop, img):
    (x, y) = extTop
    for i in range(6):
        for j in range(10):
            if 75*i<= x and x<=75*(i+1):
                if 45*j<= y and y<=45*(j+1):
                    return key(i,j)
                
def key(i,j):
    (x, y) = (i,j)
    
    dict = {'!':(0, 0),'1':(1,0), 'Q':(2,0), 'A':(3,0), 'Z':(4,0), ':':(5,0),
            '@':(0, 1),'2':(1,1), 'W':(2,1), 'S':(3,1), 'X':(4,1), ';':(5,1),
            '#':(0, 2),'3':(1,2), 'E':(2,2), 'D':(3,2), 'C':(4,2), '"':(5,2),
            '$':(0, 3),'4':(1,3), 'R':(2,3), 'F':(3,3), 'V':(4,3), "'":(5,3),
            '%':(0, 0),'5':(1,4), 'T':(2,4), 'G':(3,4), 'B':(4,4), ',':(5,4),
            '^':(0, 5),'6':(1,5), 'Y':(2,5), 'H':(3,5), 'N':(4,5), '.':(5,5),
            '&':(0, 6),'7':(1,6), 'U':(2,6), 'J':(3,6), 'M':(4,6), '<':(5,6),
            '*':(0, 7),'8':(1,7), 'I':(2,7), 'K':(3,7), ' ':(4,7), '>':(5,7),
            "(":(0, 8),'9':(1,8), 'O':(2,8), 'L':(3,8), ' ':(4,8), '/':(5,8),
            ")":(0, 9),'0':(1,9), 'P':(2,9), ' ':(3,9), ' ':(4,9), '?':(5,9)
            }
    for key, coords in dict.items():
        if (x,y)==coords:
            return key
        
                

img = cv2.imread("C:\\Users\\Aanal Sonara\\Downloads\\Keyboard-1.jpg")

res = preprocess(img)
        
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame1 = cap.read()
    cv2.imshow('video', frame1)
    print(frame1.shape)
    
    time.sleep(1)
    
    _, frame2 = cap.read()
    print(frame2.shape)
    
    diff = cv2.subtract(frame1, frame2)
    b, g, r = cv2.split(diff)
    
    if cv2.countNonZero(b)<=5 and cv2.countNonZero(g)<=5 and cv2.countNonZero(r)<=5 :
        img2 = preprocess(frame2)

        img_diff = cv2.absdiff(res,img2)
        img_diff = cv2.cvtColor(img_diff, cv2.COLOR_BGR2GRAY)
        diff_contour, _ = cv2.findContours(img_diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        c = max(diff_contour, key = cv2.contourArea)
        extTop = tuple(c[c[:,:,1].argmin()][0])

        key = check_key(extTop, res)
        
cap.release()
cv2.waitKey(1000000)

cv2.destroyAllWindows()```
