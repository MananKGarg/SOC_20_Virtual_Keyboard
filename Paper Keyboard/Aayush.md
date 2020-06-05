## Instructions for code
- The Whole Keyboard should be visible on the frame for code to work.
- Sometimes the perspective transform may be buggy re-run the code.

## Code
```python
import numpy as np
import cv2
import time
from datetime import datetime

bgSubtractor = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=30, detectShadows=False)

key_l = np.array(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '1', '2', '3', '4', '5', '6', '7', '8',
                  '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h',
                  'j', 'k', 'l', 'BSP', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ' ', ' ', 'shift', ':', ';', '\"', '\'',
                  ',', '.', '<', '>', '/', '?'])
keys = np.reshape(key_l, (6, 10))
text = ['']
shift = False
i, j = -1, -1
old_i, old_j = -1, -1
x, y = -2, -2
present = datetime.now()
start = datetime.now()


def get_ROI(image):
    """
    finds the four corners of the keyboard
    :param image: frame containing keyboard
    :return: four corners in order Top-Left, Top-Right, Bottom-Left, Bottom-right
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 6)
    gblur = cv2.GaussianBlur(thresh, (5, 5), 0)
    edge = cv2.Canny(gblur, 100, 200)                                           # All the steps are done so that perspective transform
    cont, hie = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # and finding contours is easy
    c = max(cont, key=cv2.contourArea)                                          # assuming keyboard has max contour area
    approx = cv2.approxPolyDP(c, 20, True)
    pts = np.float32([approx[0][0], approx[3][0], approx[1][0], approx[2][0]])
    return pts


def bgSubMasking (frame):
    """
    used for subracting the background to only get hand
    :param frame: frame containing moving object
    :return: threshed image of moving object
    """
    fgmask = bgSubtractor.apply(frame, learningRate=0)
    kernel = np.ones((4, 4), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=2)     # The effect is to remove the noise in the background
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)    # To close the holes in the objects
    fgmask = cv2.bitwise_and(frame, frame, mask=fgmask)                         # Apply the mask on the frame
    grayMask = cv2.cvtColor(fgmask, cv2.COLOR_BGR2GRAY)                         # Converting to gray to apply threshold
    ret, thresh = cv2.threshold(grayMask, 20, 255, 0)                           # applying threshold according to our hand
    return thresh

def getMaxContours(img):
    """
    finds the contour having max area
    :param img: image whose contour have to found
    :return: list containg contour points of max contour area
    """
    contours, hiearchy = cv2.findContours(img, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    maxIndex = 0
    maxArea = 0
    if len(contours) > 0:
        for i in range(len(contours)):
            cnt = contours[i]
            area = cv2.contourArea(cnt)
            if area > maxArea:
                maxArea = area
                maxIndex = i
        return contours[maxIndex]
    else:
        return None

def update_text(char):
    """
    This updates the text on the screen (NOTE: Text position have to be set manually)
    :param char: the text to printed on screen
    :return: Nothing
    """
    global shift
    if char == 'BSP':
        text.pop()
    elif char == 'shift':
        shift = not shift
    else:
        if shift:
            text.append(char.upper())
        else:
            text.append(char)

def key_value(contour):
    """
    finds on which key the tip of our finger lies
    :param contour: contour which have max area on the moving hand frame
    :return: key id
    """
    if (200 < cv2.contourArea(contour) < 140000):
        cv2.drawContours(hand_thresh, contour, -1, (0, 255, 0), 2)
        a = np.array(contour[:, 0])                                     # array of all points in contour
        y = list(a[:, 1])                                               # list of y coordinates
        pt = (a[y.index(min(y)), :])                                    # minimum y co-ordinate
        x, y = pt
        i = x // 50
        j = y // 50
        return (i, j)
    else:
        return (-1, -1)

def key_pressed(cont):
    """
    finds whether a key is pressed or not.
    :param cont: contour which have max area on the moving hand frame
    :return: Nothing if key is pressed just updates the text on screen
    """
    global start, present, i, j, old_j, old_i

    old_i, old_j = i, j
    i, j = key_value(cont)
    if i >= 0 and (old_i, old_j) != (i, j):
        start = datetime.now()
    present = datetime.now()
    diff = present - start
    if i >= 0 and diff.microseconds >= 600000:
        start = datetime.now()
        update_text(keys[j][i])

# url = "http://192.168.43.1:8080/video"

cap = cv2.VideoCapture(url)
# fourcc = cv2.VideoWriter_fourcc(*'MP4V');   #or fourcc = cv2.VideoWriter_fourcc('X','V','I','D');
# out = cv2.VideoWriter('Ritika.mp4', fourcc, 20.0, (int(cap.get(3)),int(cap.get(4))));

time.sleep(1)
screenpts = np.float32([[0, 0], [499, 0], [0, 299], [499, 299]])

for i in range(10):
    _, frame1 = cap.read()

pts = get_ROI(frame1)                                               # gets point for perspective transform
matrix = cv2.getPerspectiveTransform(pts, screenpts)                # transform matrix
keyboard1 = cv2.warpPerspective(frame1, matrix, (500, 300))         # initial keyboard without hand just for reference to verify perspective transform is correct

while cap.isOpened():
    ret2, frame2 = cap.read()
    keyboard2 = cv2.warpPerspective(frame2, matrix, (500, 300))
    hand_thresh = bgSubMasking(keyboard2)                           # threshed image of the hand
    maxContour = getMaxContours(hand_thresh)
    if maxContour is not None:
        key_pressed(maxContour)
    if shift:
        cv2.rectangle(frame2, (730, 460), (808, 540), (0, 255, 0), 5)   # puts rectangle on shift key have to set manually
    cv2.putText(frame2, ''.join(text), (50, 670), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)    # point of starting text to be set manually
    cv2.imshow('key2', keyboard2)
    cv2.imshow('frame', frame2)
    # out.write(frame2)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# out.release()
cap.release()
cv2.destroyAllWindows()
```
