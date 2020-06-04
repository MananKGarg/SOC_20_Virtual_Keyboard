## Code

```python
import cv2 as cv
import numpy as np
import time

keys=np.array([['!','@','#','$','%','^','&','*','(',')'],
               ['1','2','3','4','5','6','7','8','9','0'],
               ['Q','W','E','R','T','Y','U','I','O','P'],
               ['A','S','D','F','G','H','J','K','L','\n'],
               ['Z','X','C','V','B','N','M',' ',' ','shift'],
               [':',';','"',"'",',','.','<','>','/','?']])

video = cv.VideoCapture('Typing.mp4')

key = 'A'

CAPS_ON = False
t1 = time.time()

def caps():
    global CAPS_ON
    CAPS_ON = not CAPS_ON

def transform(frame):
    initial_corners = np.array(([, ], [, ], [, ], [, ]), dtype = np.float32)
    required_corners = np.array(([1280, 720], [0, 720], [1280, 0], [0, 0]), dtype = np.float32)
    transform = cv.getPerspectiveTransform(initial_corners, required_corners)
    final_frame = cv.warpPerspective(frame, transform, (1280, 720))
    finger = cv.bgsegm.createBackgroundSubtractorMOG().apply(final_frame)
    finger = cv.morphologyEx(finger,cv.MORPH_OPEN,np.ones((5,5),np.uint8))
    return finger

def get_key(top):
    return keys[top[1]//120][top[0]//128]

def get_output(current, key):
    global CAPS_ON
    if key == current:
        if time.time() - t1 >= 0.5:
            if key == 'shift':
                caps()
            else:
                if CAPS_ON:
                    output += current
                else:
                    output += current.lower()
                key = current

    return key

output = ''
while (video.isOpened()):

    _,frame=video.read()
    top = [2000, 2000]

    finger = transform(frame)
    contours,_ = cv.findContours(finger,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        frame = cv.putText(frame, output, (,), cv.FONT_HERSHEY_COMPLEX, 2, (0,0,0), thickness=3)
        cv.imshow('frame', frame)
        continue

    for contour in contours:

        if cv.contourArea(contour) < 1000:
            continue

        if np.amin(contour[:, 0][:, 1]) < top[1]:
            top = contour[:, 0][np.argmin(contour[:, 0][:, 1])]

    current = get_key(top)
    if key != current:
        key = current:
        t1 = time.time()

    key = get_output(current, key)

    frame = cv.putText(frame, output, (,), cv.FONT_HERSHEY_COMPLEX, 2, (0,0,0), thickness=3)
    cv.imshow('frame',frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
```

## Note
This code is complete but may not be fully functional, some bugs might be there and some parametric optimisations are to be done. 
It is because I couldn't check my code on a paper keyboard since I was not able to obtain a printout of the keyboard. 
I have been waiting for it for more than 15 days now, but still couldn't get it.
