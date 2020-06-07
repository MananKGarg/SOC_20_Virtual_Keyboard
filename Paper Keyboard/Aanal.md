## Paper Keyboard
We have made this keyboard following a series of steps:
* Take the frame
* Edit the frame to get only the keyboard (assuming that contour has maximum area).
* Now start recording.
* For each frame process it, and find difference between that frame and orginial keyboard.
* Find the top most point of contour of this difference
* Conforming whether key is pressed.
```python
import numpy as np
import cv2
import time
import datetime

i, j, c_j, c_i = 0,0,0,0 

def preprocess(img):
    img = cv2.resize(img, (450, 450))

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #converting to grayscale
    
    img_guass = cv2.GaussianBlur(img_gray, (5,5), 0) #applying guass blur

    img_thresh = cv2.adaptiveThreshold(img_guass, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 201, 5) #apply adaptive thresholding
    
    img_contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # obtaining the contours
    for cnt in img_contours:
        area = cv2.contourArea(cnt)
        if area>30000:  #this condition might be too high but I required that on the image I used
            
            approx = cv2.approxPolyDP(cnt, 20, True)
            #cv2.drawContours(img, [approx], 0, (255, 0, 0), 5) #to check
            pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])
            screen = np.float32([[0,0],[449, 0], [0,449], [449, 449],])
            
            matrix = cv2.getPerspectiveTransform(pts, screen)
            result = cv2.warpPerspective(img, matrix, (img.shape[0], img.shape[1])) #get the perspective image
    (rows, cols) = result.shape[:2] 
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1) #some images were rotated so I added this to get back the original configuration
    result = cv2.warpAffine(result, M, (cols, rows)) 
    
    return img

def pressed_key(c_i, c_j):
    dict_key = {'!':(0, 0),'1':(1,0), 'Q':(2,0), 'A':(3,0), 'Z':(4,0), ':':(5,0),
            '@':(0, 1),'2':(1,1), 'W':(2,1), 'S':(3,1), 'X':(4,1), ';':(5,1),
            '#':(0, 2),'3':(1,2), 'E':(2,2), 'D':(3,2), 'C':(4,2), '"':(5,2),
            '$':(0, 3),'4':(1,3), 'R':(2,3), 'F':(3,3), 'V':(4,3), "'":(5,3),
            '%':(0, 0),'5':(1,4), 'T':(2,4), 'G':(3,4), 'B':(4,4), ',':(5,4),
            '^':(0, 5),'6':(1,5), 'Y':(2,5), 'H':(3,5), 'N':(4,5), '.':(5,5),
            '&':(0, 6),'7':(1,6), 'U':(2,6), 'J':(3,6), 'M':(4,6), '<':(5,6),
            '*':(0, 7),'8':(1,7), 'I':(2,7), 'K':(3,7), ' ':(4,7), '>':(5,7),
            "(":(0, 8),'9':(1,8), 'O':(2,8), 'L':(3,8), ' ':(4,8), '/':(5,8),
            ")":(0, 9),'0':(1,9), 'P':(2,9), ' ':(3,9), '':(4,9), '?':(5,9)
            }
    #this dictionary is only to store positions of keys
    for i in range(6):
        if i*75<=c_i and 75*(i+1)>c_i:
            for j in range(10):
                if j*45<=c_j and 45*(j+1)>c_j:
                    x, y = i, j #store the row and column number of the key
                    
    for key, coords in dict_key.items():
        if (x, y)==coords: #now for that (i, j) return the key
            return key
                
                    
def top_point(c):
    extTop = tuple(c[c[:,:,1].argmin()][0])
    return extTop    #find the highest point of contour
                
def check_key(c):
    global c_i, c_j, i, j
    (c_i, c_j) = (i,j) #they are same
    (i, j) = top_point(c)    #now their value changes
    if (c_i, c_j) != (i,j):  # if they are not same it means that key has been changed
        current_time = datetime.now() #note the time for as long as the points are same that is our top most point is in desired key region
    future_time = datetime.now()
    diff = future_time - current_time
    if diff.microseconds>= 2000000: #if difference is more than two seconds consider it pressed
        return pressed_key(c_i, c_j) #now pass co ordinates of when the key was pressed (since (i, j) changes only then can we consider it pressed) 



cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, frame = cap.read()
    frame = preprocess(frame) #process the frame
    pen = cv2.createBackgroundSubtractorMOG2(detectShadows = False).apply(frame)
        
    c = max(frame, key = cv2.contourArea) #find the one with maximum area

    letter = check_key(c, frame)
    frame = cv2.putText(frame, ''.join(letter), (30,30), cv2.FONT_HERSHEY_COMPLEX, 5, (255, 0, 0)) #add the letter
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break 
      
cap.release()
cv2.destroyAllWindows()

```
I have tried to be as accurate as possible, but I faced errors in detecting contours and top most point and lack of a proper paper keyboard to detect proper contours. 
