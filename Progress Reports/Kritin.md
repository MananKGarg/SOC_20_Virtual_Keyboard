# VIRTUAL KEYBOARD
## AIM
The output of project is to build a laser projected keyboard which when typed upon, outputs the corresponding key press onto a monitor in real time.


## PROGRESS REPORT
* 23rd March to 1st April 2020
  - I started learning python for first time by watching youtube videos and solving question on geekforgeeks and other platforms.
  - Installed pycharm and started using it.
  - Made a github profile, learnt basics of using Github .
  - I was unable to install ubuntu on my laptop , therefore worked on windows only.
  
* 2nd to 5th April 2020
  - Completed problem number 1 from the 1st assignment. 
  
* 7th to 10th April 2020
  - Saw the solutions of the assignment and also the answers provided by other mentees.
  - Also worked on other 3 problems that i was not able to complete
  
* 11th to 21th April 2020
  - Learned [OpenCV](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K) and various image processing techniques.

* 23rd to 27th April 2020
  - Invisibility Cloak Project. The code:
``` python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)                                        # accessing the webcam
background = 0
fourcc = cv2.VideoWriter_fourcc(*'XVID')                         # naming a variable to store codec information
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (640,480))     # creating a variable to store video
for i in range(30):                                              # iterating many times to get a averaged background image
    return_val, background = cap.read()
    if return_val == False:
        continue

while (cap.isOpened()):                                          # initiating webcam
    return_val, img = cap.read()
    if not return_val:                                           # checking whether webcam is working
        break

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)                   # converting the image into hsv from BGR colour scheme

    lower = np.array([0, 120, 70])                               # specifying upper and lower limit for red colour
    upper = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower, upper)                       # segmenting objects with red colour by masking(the clock which is red will be masked by white rest by black)

    lower = np.array([170, 120, 70])
    upper = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower, upper)

    mask1 = mask1 + mask2                                        # combining segmented red colour objects from both limits
    mask2 = cv2.bitwise_not(mask1)                               # creating an image where clock is black and rest is white

    res1 = cv2.bitwise_and(background, background, mask=mask1)   # taking and between background and mask1 to get an image where clock part shows background and rest is black
    res2 = cv2.bitwise_and(img, img, mask=mask2)                 # taking and between image and mask2 to get an image where clock part is black and rest is as it is 
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)          # adding both previous variables to get the final output

    out.write(final_output)                                      # saving the video to out
    cv2.imshow("clock", final_output)
    k = cv2.waitKey(10)
    if k == 27:                                                  # program exits by pressing ESC key
        break
cap.release()
out.release()
cv2.destroyAllWindows()
```


* 27th April - 10th May 2020
  - Experimenting with opencv to create different stuff.
  
* 10th May - 25th May 2020
  - Started on the Sudoku Solver Project
  - Completed the OpenCV part of the project (i.e. was able to extract digits out of 81 boxes)
  - Worked on the digit recognition part but was not able to complete it. 
  
* 25th May - 31st May 2020
  - Started working on the Virtual Keyboard
  
 
