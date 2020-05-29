### Code:
```python
import cv2
import numpy as np
import operator
from keras.models import load_model
model = load_model('customised0.h5')
font = cv2.FONT_HERSHEY_COMPLEX
tried = False
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (640, 480))
'''
Names: 
corners - the coordinates the vertices of the sudoku in the input image
sudoku - the transformed image of the sudoku
cells - an array of images of each cell
puzzle - the input sudoku in array form
solution - the solved sudoku in array form
augmented_img - the transformed image of the sudoku with the digits augmented
'''


def put_text(i, j, num, inp_sudoku):
    x = 50*i + 15
    y = 50*j + 40
    cv2.putText(inp_sudoku, str(num), (x, y), font, 1, (0, 255, 0), thickness=3)
    return True


def fill_spaces(inp_sudoku, inp, solved):
    for i in range(9):
        for j in range(9):
            if inp[i][j] == 0:
                put_text(j, i, solved[i, j], inp_sudoku)


def find_digit(image):
    image = image.reshape((1, 28, 28, 1))
    if np.mean(image) < 25:
        return 0
    prediction = model.predict_classes(image)
    return prediction[0]


def free(arr, empty):
    for i in range(9):
        for j in range(9):
            if arr[i, j] == 0:
                empty[0] = i
                empty[1] = j
                return True
    return False


def col_safe(j, arr, num):
    for i in range(9):
        if arr[i][j] == num:
            return False
    return True


def row_safe(i, arr, num):
    for j in range(9):
        if arr[i][j] == num:
            return False
    return True


def nonet_safe(i, j, arr, num):
    i1 = i - (i % 3)
    j1 = j - (j % 3)
    return not (num in arr[i1:i1 + 3, j1:j1 + 3])


def is_safe(i, j, arr, num):
    return col_safe(j, arr, num) and row_safe(i, arr, num) and nonet_safe(i, j, arr, num)


def fill_values(arr):
    empty = [0, 0]
    if not free(arr, empty):
        return True
    x, y = empty
    for num in range(1, 10):
        if is_safe(x, y, arr, num):
            arr[x, y] = num
            if fill_values(arr):
                return True
            arr[x, y] = 0
    return False


def solve(inp_sudoku):
    arr = inp_sudoku.copy()
    solved = fill_values(arr)
    if solved:
        print(arr)
        return arr
    print('Cant Solve !')
    return inp_sudoku


def cell(i, j, inp_sudoku):
    lp, rp, up, dp = (7, 8, 7, 6)
    if i % 3 == 0:
        up += 5
    if j % 3 == 0:
        lp += 2
    digit = inp_sudoku[50*i + up:50*(i+1) - dp, 50*j + lp:50*(j+1) - rp]
    return cv2.resize(digit, (28, 28))


vid = cv2.VideoCapture(0)
kernel = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]],
                  dtype='uint8')
standard = np.array([[0, 0], [450, 0], [450, 450], [0, 450]], dtype='float32')

while True:
    q = cv2.waitKey(1)
    if q == ord('q'):
        break
    _, frame = vid.read()
    l, b, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    dilate = cv2.dilate(thresh, kernel)
    _, contours, _ = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    outline = contours[0]
    bottom_right, _ = max(enumerate([pt[0][0] + pt[0][1] for pt in outline]), key=operator.itemgetter(1))
    bottom_left, _ = min(enumerate([pt[0][0] - pt[0][1] for pt in outline]), key=operator.itemgetter(1))
    top_left, _ = min(enumerate([pt[0][0] + pt[0][1] for pt in outline]), key=operator.itemgetter(1))
    top_right, _ = max(enumerate([pt[0][0] - pt[0][1] for pt in outline]), key=operator.itemgetter(1))
    corners = np.array([outline[top_left][0],
                       outline[top_right][0],
                       outline[bottom_right][0],
                       outline[bottom_left][0]],
                       dtype='float32')

    transform = cv2.getPerspectiveTransform(corners, standard)
    inv_transform = cv2.getPerspectiveTransform(standard, corners)
    sudoku = cv2.warpPerspective(gray, transform, (450, 450))
    mblur = cv2.medianBlur(sudoku, 5)
    sudoku = cv2.adaptiveThreshold(mblur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 3)
    cells = np.array([[cell(p, q, sudoku) for p in range(9)] for q in range(9)])

    if q == ord('s'):
        tried = True
        augmented_img = cv2.warpPerspective(frame, transform, (450, 450))
        puzzle = np.array([[find_digit(cells[i, j]) for i in range(9)] for j in range(9)], dtype='uint8')
        solution = solve(puzzle)
        fill_spaces(augmented_img, puzzle, solution)

    if tried:
        in_place = cv2.warpPerspective(augmented_img, inv_transform, (b, l))
        sud_mask = np.ones_like(sudoku, dtype='uint8') * 255
        sud_mask = cv2.warpPerspective(sud_mask, inv_transform, (b, l))
        rest_mask = cv2.bitwise_not(sud_mask)
        rest = cv2.bitwise_and(frame, frame, mask=rest_mask)
        ans = cv2.add(rest, in_place)
        frame = ans
    cv2.imshow('sudoku', sudoku)
    cv2.imshow('video', frame)
    out.write(frame)
cv2.waitKey(1)
vid.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

```
