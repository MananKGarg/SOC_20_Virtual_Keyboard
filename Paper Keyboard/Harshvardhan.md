import numpy as np
import cv2
import time
from datetime import datetime

bg = cv2.createBackgroundSubtractorMOG2(history=10, varThreshold=30, detectShadows=False)

keyboard=np.array([['!','@','#','$','%','^','&','*','(',')'],
                   ['1','2','3','4','5','6','7','8','9','0'],
                   ['Q','W','E','R','T','Y','U','I','O','P'],
                   ['A','S','D','F','G','H','J','K','L','BACK'],
                   ['Z','X','C','V','B','N','M',' ',' ','CAPS'],
                   [':',';','\"','\'',',','.','<','>','/','?']])
keys = np.reshape(keyboard, (6, 10))
text = ['']
shift = False
i, j = -1, -1
old_i, old_j = -1, -1
x, y = -2, -2
present = datetime.now()
start = datetime.now()

def bgMasking (frame):
    fgmask = bg.apply(frame, learningRate=0)
    kernel = np.ones((4, 4), np.uint8)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel, iterations=2)     # Removing noise in the background
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel, iterations=2)
    fgmask = cv2.bitwise_and(frame, frame, mask=fgmask)                         # Applying mask
    grayMask = cv2.cvtColor(fgmask, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grayMask, 20, 255, 0)                           # Applying threshold according to our hand
    return thresh

def get_RegionI(image):
    grayScale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(grayScale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 6)
    blur = cv2.GaussianBlur(thresh, (5, 5), 1)
    edge = cv2.Canny(blur, 100, 200)                                           # Perspective transform is being used here throughout
    cont, hie = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cont, key=cv2.contourArea)                                          # assuming keyboard has max contour area
    approx = cv2.approxPolyDP(c, 20, True)
    pts = np.float32([approx[0][0], approx[3][0], approx[1][0], approx[2][0]])
    return pts



def getContours(img):
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

def key_value(contour):
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

def Utext(char):
    global caps
    if char == 'BACK':
        text.pop()
    elif char == 'CAPS':
        caps = not caps
    else:
        if caps:
            text.append(char.upper())
        else:
            text.append(char)


def key_pressed(cont):
    global start, present, i, j, old_j, old_i

    old_i, old_j = i, j
    i, j = key_value(cont)
    if i >= 0 and (old_i, old_j) != (i, j):
        start = datetime.now()
    present = datetime.now()
    diff = present - start
    if i >= 0 and diff.microseconds >= 600000:
        start = datetime.now()
        Utext(keys[j][i])


cap = cv2.VideoCapture(0)

time.sleep(1)
screenpts = np.float32([[0, 0], [499, 0], [0, 299], [499, 299]])

for i in range(10):
    _, frame1 = cap.read()

    pts = get_RegionI(frame1)                                          # gets point for perspective transform
    matrix = cv2.getPerspectiveTransform(pts, screenpts)                #Transformation
    keyboard1 = cv2.warpPerspective(frame1, matrix, (500, 300))         # initial keyboard without hand just for reference to verify perspective transform is correct

    while cap.isOpened():
        ret2, frame2 = cap.read()
        keyboard2 = cv2.warpPerspective(frame2, matrix, (500, 300))
        hand_thresh = bgMasking(keyboard2)                           #Image of hand distinguished
        maxContour = getContours(hand_thresh)
        if maxContour is not None:
            key_pressed(maxContour)
        if shift:
            cv2.rectangle(frame2, (730, 460), (808, 540), (0, 255, 0), 5)           # puts rectangle on CAPS key have to set manually
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
