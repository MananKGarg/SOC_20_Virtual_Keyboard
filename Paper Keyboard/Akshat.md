# How to Use Keyboard

1. Take an object(with a colored tip) to point a key.(I'm using orange colored tip)
2. Tap the key and wait for half a sec to print the key
3. Make sure you have a stable camera

[Here](https://github.com/ViraAkshat/Virtual_Keyboard/tree/master/Paper%20Keyboard) is my try

## How it works
1. It calculates the corner points of keyboard and brings it in perspective using contours
2. Then it locates the colored tip and calculates its centroid
3. If the tip is on a key for half a sec then it registers the key
4. Then the key pressed is added to a text string which is also displayed on the video

## Code

```python
import numpy as np
import cv2
import time

caps = np.array([['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
                 ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                 ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                 ['A', 'S ', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '\n'],
                 ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', ' ', 'caps'],
                 [':', ';', '"', '\'', ',', '.', '<', '>', '/', '?']])
keys = np.array([['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
                 ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                 ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                 ['a', 's ', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\n'],
                 ['z', 'x', 'c', 'v', 'b', 'n', 'm', ' ', ' ', 'caps'],
                 [':', ';', '"', '\'', ',', '.', '<', '>', '/', '?']])
text = ''
CAPS, t1, t2, pressed_once, key = False, 0, 0, 0, (0, 0)

cap = cv2.VideoCapture('vid4.mp4')
four_cc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('keyboard.avi', four_cc, 20.0, (1280, 720))


# To bring keyboard in perspective
def keyboard_perspective(image):
    """

    :param image: The image containing the keyboard
    :return: keyboard in perspective and corner points of keyboard
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thg = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 71, 7)
    gauss = cv2.GaussianBlur(thg, (5, 5), 0)

    # Finds the contour with max area
    contours, h = cv2.findContours(gauss, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxArea, maxContour = 0, contours[0]
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > maxArea:
            maxContour = contour
        maxArea = max(area, maxArea)

    epsilon = 0.1 * cv2.arcLength(maxContour, True)
    approx = cv2.approxPolyDP(maxContour, epsilon, True)    # Gives proper corner locations of keyboard
    pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])
    d = np.float32([[0, 0], [719, 0], [0, 1279], [719, 1279]])
    matrix = cv2.getPerspectiveTransform(pts, d)
    final = cv2.warpPerspective(image, matrix, (720, 1280))
    final = cv2.rotate(final, cv2.ROTATE_90_COUNTERCLOCKWISE)

    return final, approx    # Returns keyboard in perspective and its corner positions


# To bring frame in perspective
def perspective(image, pos):
    """

    :param image: image containing keyboard and pointer
    :param pos: corner points of keyboard
    :return: keyboard in perspective/removes excess background
    """
    pts = np.float32([pos[1][0], pos[0][0], pos[2][0], pos[3][0]])
    d = np.float32([[0, 0], [719, 0], [0, 1279], [719, 1279]])
    matrix = cv2.getPerspectiveTransform(pts, d)
    final = cv2.warpPerspective(image, matrix, (720, 1280))
    final = cv2.rotate(final, cv2.ROTATE_90_COUNTERCLOCKWISE)

    return final


# To find coordinates of colored tip of pointer
def coordinates(img):
    """

    :param img: image containing pointer over a key
    :return: position of pointer's colored tip
    """
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low = np.array([9, 160, 120])            # Color range of tip of pointer
    high = np.array([12, 255, 250])          #
    color = cv2.inRange(img, low, high)      # Location of tip

    M = cv2.moments(color)                   #
    if M["m00"] != 0:                        #
        x = int(M["m10"] / M["m00"])         # Calculation of centroid of tip
        y = int(M["m01"] / M["m00"])         #
    else:                                    #
        x, y = 0, 0                          #

    return x, y


# To find which key is pressed
def is_key_pressed(x, y):
    """

    :param x: x coordinate of pointer's tip
    :param y: y coordinate of pointer's tip
    Finds the key which is pressed
    """
    global t1, t2, key, pressed_once
    xKey = x//128
    yKey = y//120

    enter_new_cell = (key != (yKey, xKey))
    if enter_new_cell:
        t1 = time.monotonic()                # Time of entry in new cell
        key = (yKey, xKey)                   # Coordinates of new cell
        pressed_once = 0
    else:
        t2 = time.monotonic()                # t2 - t1 gives time spent in a particular cell

    if (t2 - t1) > 0.8 and pressed_once == 0:
        pressed_once += 1


# Finds the keyboard position
_, keyboard = cap.read()
keyboard = cv2.resize(keyboard, (1280, 720))
keyboard = cv2.rotate(keyboard, cv2.ROTATE_180)  # Change of orientation, so that it looks upright
keyboard, keyPos = keyboard_perspective(keyboard)
keyPos2 = [[0], [0], [0], [0]]                   # This will be used to crop video to show keyboard with some padding
keyPos2[0][0] = keyPos[0][0] + (-100, -100)
keyPos2[1][0] = keyPos[1][0] + (-100, 100)
keyPos2[2][0] = keyPos[2][0] + (100, 100)
keyPos2[3][0] = keyPos[3][0] + (100, -100)

while cap.isOpened():

    ret, frame = cap.read()                      # Reads the video
    if ret is False:
        break

    frame = cv2.resize(frame, (1280, 720))       # Resizing the video
    frame = cv2.rotate(frame, cv2.ROTATE_180)    # Tweak this based on orientation of video
    cv2.imshow('one', frame)

    res = perspective(frame, keyPos)             # Brings keyboard in perspective
    frame = perspective(frame, keyPos2)
    cv2.imshow('result', res)

    cx, cy = coordinates(res)                    # Finds the center of pointer
    is_key_pressed(cx, cy)                       # Checks whether key is pressed

    if pressed_once == 1 and cx != 0:
        if key == (4, 9):                        # Switches caps on and off
            CAPS = not CAPS
            pressed_once += 1
        else:
            if CAPS:
                text += caps[key]
            else:
                text += keys[key]
        pressed_once += 1
        print(text)

    # To add new line while using putText function
    y0, dy = 650, 40
    for i, line in enumerate(text.split('\n')):
        yt = y0 + i * dy
        frame = cv2.putText(frame, line, (50, yt), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 0), 2)

    # To add caps_on light
    if CAPS:
        frame = cv2.circle(frame, (1000, 440), 4, (0, 255, 0), -1)

    cv2.imshow('frame', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

```
