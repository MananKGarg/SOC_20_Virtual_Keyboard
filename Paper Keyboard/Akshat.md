# How to Use Keyboard

1. Take a colored object to point a key.(I'm using orange color)
2. Tap the key and wait for 1sec to print the key

## Code

```python
import numpy as np
import cv2
import time

caps = np.array([['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
                 ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                 ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                 ['A', 'S ', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '\n'],
                 ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', ' ', ''],
                 [':', ';', '"', '\'', ',', '.', '<', '>', '/', '?']])
keys = np.array([['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
                 ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                 ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                 ['a', 's ', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\n'],
                 ['z', 'x', 'c', 'v', 'b', 'n', 'm', ' ', ' ', ''],
                 [':', ';', '"', '\'', ',', '.', '<', '>', '/', '?']])
text = ''
s, t1, t2, pressed_once, key = 0, 0, 0, 0, (0, 0)

cap = cv2.VideoCapture('vid4.mp4')


# To bring keyboard in perspective
def keyboardPerspective(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thg = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 71, 7)
    gauss = cv2.GaussianBlur(thg, (5, 5), 0)

    contours, h = cv2.findContours(gauss, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxArea, maxContour = 0, contours[0]
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > maxArea:
            maxContour = contour
        maxArea = max(area, maxArea)

    epsilon = 0.1 * cv2.arcLength(maxContour, True)
    approx = cv2.approxPolyDP(maxContour, epsilon, True)
    pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])
    d = np.float32([[0, 0], [719, 0], [0, 1279], [719, 1279]])
    matrix = cv2.getPerspectiveTransform(pts, d)
    final = cv2.warpPerspective(image, matrix, (720, 1280))
    final = np.rot90(final)

    return final, approx


# To bring frame in perspective
def perspective(image, pos):
    pts = np.float32([pos[1][0], pos[0][0], pos[2][0], pos[3][0]])
    d = np.float32([[0, 0], [719, 0], [0, 1279], [719, 1279]])
    matrix = cv2.getPerspectiveTransform(pts, d)
    final = cv2.warpPerspective(image, matrix, (720, 1280))
    final = np.rot90(final)

    return final


# To find coordinates of fingertip
def coordinates(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low = np.array([9, 160, 120])
    high = np.array([12, 255, 250])

    color = cv2.inRange(img, low, high)
    M = cv2.moments(color)
    if M["m00"] != 0:
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
    else:
        x, y = 0, 0

    return x, y


# To find which key is pressed
def is_key_pressed(x, y):
    global t1, t2, key, pressed_once
    xrange = np.arange(0, 1281, step=128)
    yrange = np.arange(0, 721, step=120)
    xKey, yKey = 0, 0

    for i in range(0, 10):
        if xrange[i] < x < xrange[i + 1]:
            xKey = i
    for j in range(0, 6):
        if yrange[j] < y < yrange[j + 1]:
            yKey = j

    if key == (yKey, xKey):
        enter_new_cell = False
    else:
        key = (yKey, xKey)
        enter_new_cell = True
        pressed_once = 0

    if enter_new_cell:
        t1 = time.monotonic()
    else:
        t2 = time.monotonic()

    if (t2 - t1) > 0.8 and not pressed_once:
        pressed_once += 1


# Finds the keyboard position
_, keyboard = cap.read()
keyboard = cv2.resize(keyboard, (1280, 720))
keyboard = np.rot90(keyboard)
keyboard = np.rot90(keyboard)
keyboard, keyPos = keyboardPerspective(keyboard)

while cap.isOpened():

    ret, frame = cap.read()  # Reads the video
    if ret is False:
        break

    frame = cv2.resize(frame, (1280, 720))  # Resizing the video
    frame = np.rot90(frame)                 # Tweak this based on orientation of video
    frame = np.rot90(frame)
    cv2.imshow('one', frame)

    res = perspective(frame, keyPos)  # Brings keyboard in perspective
    cv2.imshow('result', res)

    cx, cy = coordinates(res)  # Finds the center of pointer
    is_key_pressed(cx, cy)     # Checks whether key is pressed

    if pressed_once == 1 and cx != 0:
        if key == (4, 9):
            if s == 0:
                s = 1
                pressed_once += 1
            else:
                s = 0
                pressed_once += 1
        else:
            if s == 1:
                text = text + caps[key]
                pressed_once += 1
                print(text)
            else:
                text = text + keys[key]
                pressed_once += 1
                print(text)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



```
