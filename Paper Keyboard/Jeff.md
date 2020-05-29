### Code:
```python
import cv2
import numpy as np
from datetime import datetime as dt

# fourcc = cv2.VideoWriter_fourcc(*'X264')
url='http://192.168.43.1:8080/video'
vid = cv2.VideoCapture(url)
# out = cv2.VideoWriter('video.mp4', fourcc, 30.0, (int(vid.get(3)), int(vid.get(4))))
points = []                             # stores the corners of keyboard in the frame
cell_ID = (-1, -1)                      # initialising cell_ID to (-1, -1)
old_cell_ID = (-2, -2)
transform = None
flag = False
caps_on = False
shifted = False
cv2.namedWindow('video')
key_dimentions = np.array([[0, 0], [600, 0], [600, 360], [0, 360]], np.float32)
start = dt.now()
present = dt.now()
shift_start = dt.now()
text = ['|']
keyboard = np.zeros((600, 360), 'uint8')

cap_keys = {0: '!',  1: '@',  2: '#',  3: '$',  4: '%',  5: '^',  6: '&',  7: '*',  8: '(',  9: ')',
            10: '1', 11: '2', 12: '3', 13: '4', 14: '5', 15: '6', 16: '7', 17: '8', 18: '9', 19: '0',
            20: 'Q', 21: 'W', 22: 'E', 23: 'R', 24: 'T', 25: 'Y', 26: 'U', 27: 'I', 28: 'O', 29: 'P',
            30: 'A', 31: 'S', 32: 'D', 33: 'F', 34: 'G', 35: 'H', 36: 'J', 37: 'K', 38: 'L', 39: 'BKS',
            40: 'Z', 41: 'X', 42: 'C', 43: 'V', 44: 'B', 45: 'N', 46: 'M', 47: ' ', 48: ' ', 49: 'Shift',
            50: ':', 51: ';', 52: '"', 53: '`', 54: ',', 55: '.', 56: '<', 57: '>', 58: '/', 59: '?'}

keys = {0: '!',  1: '@',  2: '#',  3: '$',  4: '%',  5: '^',  6: '&',  7: '*',  8: '(',  9: ')',
        10: '1', 11: '2', 12: '3', 13: '4', 14: '5', 15: '6', 16: '7', 17: '8', 18: '9', 19: '0',
        20: 'q', 21: 'w', 22: 'e', 23: 'r', 24: 't', 25: 'y', 26: 'u', 27: 'i', 28: 'o', 29: 'p',
        30: 'a', 31: 's', 32: 'd', 33: 'f', 34: 'g', 35: 'h', 36: 'j', 37: 'k', 38: 'l', 39: 'BKS',
        40: 'z', 41: 'x', 42: 'c', 43: 'v', 44: 'b', 45: 'n', 46: 'm', 47: ' ', 48: ' ', 49: 'shift',
        50: ':', 51: ';', 52: '"', 53: '`', 54: ',', 55: '.', 56: '<', 57: '>', 58: '/', 59: '?'}


def extract_cell(img, cellID):
    """
    returns a threshed cell with cell_ID - (i, j) from already transformed img
    """
    i, j = cellID
    this_cell = img[60 * j + 3:60 * (j + 1) - 3, 60 * i + 3:60 * (i + 1) - 3]
    this_cell = np.uint8(this_cell)
    _, this_cell = cv2.threshold(this_cell, this_cell.mean() - 20, 255, 1)
    return this_cell


def set_corners(event, x, y, params, flags):
    """
    function to store the points of the corners of the keyboard in points.
    """
    if event==cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
cv2.setMouseCallback('video', set_corners)


def find_top_key_pressed(gray_img, transformation):
    """
    :param gray_img: the camera input
    :param transformation: the transformation from points to standard
    :return: threshed cell image,it's cell_ID, if shift pressed If not found it gives a blank cell, (-1, -1), false
    cell_ID has x in → direction and y in ↓ direction but it is reversed in array indexing
    """
    global shifted, keyboard
    keyboard = cv2.warpPerspective(gray_img, transformation, (600, 360))
    hand = cv2.absdiff(keyboard0, keyboard)
    _, hand = cv2.threshold(hand, 50, 255, 0)
    hand = cv2.erode(hand, kernel=np.ones((11, 11), 'uint8'))
    shifted = is_key_pressed(hand, (9, 4))
    flat = hand.flatten()
    m = np.argmax(flat)
    the_cell = np.zeros((54, 54), 'uint8')
    x = y = -1
    if m > 0:
        x = (m % 600)//60
        y = (m // 600)//60
        the_cell = extract_cell(keyboard0, (x, y))
    return the_cell, (x, y), shifted


def modify_text(text_list, key, shift_val):
    """
    :param text_list: Text array
    :param key: key in keys dictionary
    :param shift_val: bool is shift is pressed
    :return: no return but modifies text in the process
    """
    if caps_on:
        shift_val = True
    if key == 39:
        if len(text) > 1:
            text_list.pop()
            text_list.pop()
            text_list.append('|')
    elif key == 49:
        pass
    elif key >= 0 and shift_val:
        text_list.pop()
        text_list.append(cap_keys[key])
        text_list.append('|')
    elif key >=0:
        text_list.pop()
        text_list.append(keys[key])
        text_list.append('|')


def is_key_pressed(img, cellID):
    """
    :param img: A threshed image of the keyboard
    :param cellID: The cellID of the cell we want to check is pressed or not
    :return: bool - pressed or not
    """
    global caps_on, shift_start
    i, j = cellID
    the_cell = img[60 * j + 3:60 * (j + 1) - 3, 60 * i + 3:60 * (i + 1) - 3]
    if np.mean(the_cell[0:10, ::]) != 0:
        return False
    if np.mean(the_cell[44:54, ::]) != 0:
        if not shifted:
            shift_start = dt.now()
        shift_present = dt.now()
        shift_diff = shift_present - shift_start
        if shift_diff.seconds >= 1 and shift_diff.microseconds >= 500000:
            caps_on = caps_on ^ 1
            shift_start = dt.now()
        return True
    return False


def cell_select_timer():
    """
    does the needful when a cell is pressed for more than the given threshold
    """
    global old_cell_ID, start, present, cell_ID

    old_cell_ID = cell_ID
    cell, cell_ID, shift = find_top_key_pressed(gray, transform)
    gray[0:54, 0:54] = cell
    if cell_ID[0] >= 0 and old_cell_ID != cell_ID:
        start = dt.now()
    present = dt.now()
    diff = present - start
    if diff.microseconds >= 500000:
        start = dt.now()
        n = cell_ID[0] + 10 * cell_ID[1]
        modify_text(text, n, shift)


while True:
    _, frame = vid.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    q = cv2.waitKey(1)
    if q == ord('q'):
        break
    elif q == ord('t'):                                   # lock on to corners of the keyboard stored in points
        if len(points)!=4:
            print('error!')
            points.clear()
        else:
            print('sucess!!')
            key_points = np.array(points, dtype='float32')
            transform = cv2.getPerspectiveTransform(key_points, key_dimentions)
            inv_transform = cv2.getPerspectiveTransform(key_dimentions, key_points)
            keyboard0 = cv2.warpPerspective(gray, transform, (600, 360))
            points.clear()
    elif q == ord('c'):
        text.clear()
        text.append('|')
    elif q == ord('p'):
        print(''.join(text[:-1]))

    if transform is not None:
        cell_select_timer()

    if caps_on:                                             # highlight the shift key
        shift_img = extract_cell(keyboard0, (9, 4))
        keyboard[243:297, 543:597] = shift_img
        mask = np.ones_like(keyboard, 'uint8')*255
        key_in_space = cv2.warpPerspective(keyboard, inv_transform, (800, 480))
        mask = cv2.bitwise_not(cv2.warpPerspective(mask, inv_transform, (800, 480)))
        back = cv2.bitwise_and(gray, gray, mask=mask)
        gray = cv2.add(back, key_in_space)

    color = np.dstack((gray, gray, gray))
    cv2.putText(color, ''.join(text), (100, 50), cv2.FONT_HERSHEY_COMPLEX, 0.75, (0, 50, 255), 2)
    cv2.imshow('video', color)
    # out.write(color)

# out.release()
vid.release()
cv2.waitKey(1)
cv2.destroyAllWindows()
cv2.waitKey(1)

```
