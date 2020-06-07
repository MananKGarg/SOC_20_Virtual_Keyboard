# Paper Keyboard

```python
import cv2
import numpy as np
from datetime import datetime
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
keys = np.array([['!','@','#','$','%','^','&','*','(',')'],
               ['1','2','3','4','5','6','7','8','9','0'],
               ['q','w','e','r','t','y','u','i','o','p'],
               ['a','s','d','f','g','h','j','k','l','\n'],
               ['z','x','c','v','b','n','m',' ',' ','shift'],
               [':',';','"',"'",',','.','<','>','/','?']])
shift = False
i, j = 0, 0
initial_i, initial_j = 0, 0
start = current = datetime.now()
text = [""]
def maxContour(thresh):
    max_area = 0
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > max_area:
            max_area = cv2.contourArea(contour)
            max_contour = contour
    return max_contour

def get_key(contour):
    area = cv2.contourArea(contour)
    if(area > 800 and area < 560000):
        top = tuple(area[area[:, :, 1].argmin()][0])
        i = top[0]//128
        j = top[1]//120
        return (i, j)

def get_text(key):
    global shift
    if key == 'shift':
        shift = not shift
    else:
        if shift:
            text.append(key.upper())
        else:
            text.append(key)

def detect_keypress(contour):
    global start, current, i, j, initial_i, initial_j
    initial_i, initial_j = i, j
    i, j = get_key(contour)
    if (initial_i, initial_j) != (i, j):
        start = datetime.now()
    current = datetime.now()
    diff = current - start
    if diff.microseconds >= 500000:
        start = datetime.now()
        get_text(keys[j][i])

cap = cv2.VideoCapture("keybrd2.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    th = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 7)
    gblur = cv2.GaussianBlur(th, (5, 5), 0)  # blurring the image
    edges = cv2.Canny(gblur, 50, 150, apertureSize=3)  # canny edge detection
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 6500:
            approx = cv2.approxPolyDP(contour, 20, True)  # defining polygon with max.area
            pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])  #
            screenpts = np.float32([[0, 0], [1280, 0], [0, 720], [1280, 720]])  # performing pespective transform
            matrix = cv2.getPerspectiveTransform(pts, screenpts)  #
            warped = cv2.warpPerspective(th, matrix, (1280, 720))
            fgmask = fgbg.apply(warped)
            fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
            masked = cv2.bitwise_and(frame, frame, mask = fgmask)
            gray_mask = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)  # Converting to gray to apply threshold
            ret, thresh = cv2.threshold(gray_mask, 95, 255, 0)
            max_contour = maxContour(thresh)
            if max_contour is not None:
                detect_keypress(max_contour)
            if shift:
                cv2.circle(frame, (986,584),3, (0,255,0),-1)
            cv2.putText(frame, ''.join(text), (40, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) == 27:
                break

cap.release()
cv2.destroyAllWindows()

```
