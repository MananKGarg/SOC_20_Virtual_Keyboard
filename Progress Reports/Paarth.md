# Virtual Keyboard

## Links
---
Here are the links to all the original codes i wrote during my SoC:
* [Invisibility Cloak](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Invisibility%20Cloak/PaarthJain.md#invisibility-cloak)
* [Sudoku Solver](https://github.com/Paarth-Jain/Sudoku-Solver)
* [Virtual Keyboard](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Paper%20Keyboard/Paarth.md#code)


## Overview
---
We aim to build a laser projected keyboard which when typed upon, outputs the corresponding
key press onto a monitor in real time.


## Flow Chart
---
* We shall build the software part in python because of the extensive library support and the easily comprehendable syntax. 
* Learning basic python syntax and the relevant libraries like Numpy, Scipy, Pandas and matplotlib etc, and getting our hands dirty.
* The next step would be to learn OpenCV (open sourced- computer vision library), and ofcourse practicing the skills.

## Progress Report
---

* 23rd to 1st April 2020
  - I revised [python](https://www.learnpython.org/), and read some new topics( Error, Exception Handling ,Function arguments amongst others) 
  - Studied the [Scipy docs](https://scipy-lectures.org/) on a basic level for knowledge of the relevant libraries.
  - Already had a Github a github profile and had Ubuntu on my laptop.
  - I studied pandas from [this](https://www.youtube.com/watch?v=Iqjy9UqKKuo&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-) source.

* 2nd to 5th April 2020
  - Completed all the problems from the 1st assignment.
 
* 7th to 10th April 2020
  - Saw the solutions of the assignment and also the answers provided by other mentees.
  
* 11th to 18th April 2020
  - Learned [OpenCV](https://www.youtube.com/watch?v=kdLM6AOd2vc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K) and various image processing techniques.
  
* 19th to 23rd April 2020 
  - Updated 2 files in the OpenCV repository.
 
* 24th to 27th April 2020
  - Invisibility Cloak Project. The code:
``` python
#This code was made by Paarth Jain(4/2020)

import cv2
import numpy as np 

def nothing(x):                                                #Nothing function for cv2.createTrackbar()
pass

cap = cv2.VideoCapture(0)                                      #capturing the webcam video
_,bg = cap.read()                                              #keep the first frame empty in order to store the background

fourcc = cv2.VideoWriter_fourcc(*'XVID')                       #fourcc stores the codec information
out = cv2.VideoWriter('inv_cloak.avi',fourcc,20.0, (640,480))  #specifying the output file with the relevant arguments(
                                                               #filepath, codec, frame rate, and resolution  
 


cv2.namedWindow('Tracking')                                    # Named window for trackbars
l_h = cv2.createTrackbar('LH', 'Tracking', 126, 255, nothing)
u_h = cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing)
l_s = cv2.createTrackbar('LS', 'Tracking', 64, 255, nothing)        #creating trackbars with initial l_hsv and u_hsv values 
                                                                    #fixed in order to make it work for a pink cloth.
u_s = cv2.createTrackbar('US', 'Tracking', 255, 255, nothing)
l_v = cv2.createTrackbar('LV', 'Tracking', 127, 255, nothing)
u_v = cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while cap.isOpened():
    ret, frame = cap.read()
    if frame is None:                                         #checking whether webcam works
        break

    cv2.imshow('Frame', frame)                                # output from webcam for comparison with original result.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)              # converting to HSV format because it is easier to manipulate
                                                              #the trackbars (hsv is intuitive and easy)
    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
                                                              #getting the values from trackbars
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l_b, u_b)                        # masking the original video (the cloak area pixels become 255 and others become 0)
    mask2 = cv2.bitwise_not(mask)                            # preparing another mask which is the "not" of the first one

    res1 = cv2.bitwise_and(frame, frame, mask= mask2)        # This gives the same as original video only the cloak area is black 
    res2 = cv2.bitwise_and(bg, bg, mask= mask)               #This gives a video where cloak region is replaced by the background and rest is black.

    res = cv2.bitwise_or(res1, res2)                         # Taking the "or" of the above two results gives us the desired result.
    # cv2.imshow('mask',mask)
    cv2.imshow('result', res)   
    
    out.write(res)                                           #saving the result to out 
    
    keyboard = cv2.waitKey(100)
    if keyboard == ord('q') or keyboard == 27:               # program exits by pressing 'q' or 'esc' button
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```

* 27th April - 1st May 2020
  - Taking a look over everything that has been done till now.
  
* 20th May - 25th May 2020
  - Started on the Sudoku Solver Project(20th May)
  - Completed the OpenCV part of the project (i.e. perspective transform and extracting all 81 boxes of sudoku.(23rd May)
  - Completed the digit recognition part by making a convolutional neural network using keras.(26th May)
  - [The code](https://github.com/Paarth-Jain/Sudoku-Solver)
  
* 28th May - 31st May 2020
  - Started working on the Virtual Keyboard
* 1st June - 6th June
  - completed the [Virtual Keyboard](https://github.com/MananKGarg/SOC_20_Virtual_Keyboard/blob/master/Paper%20Keyboard/Paarth.md#code)
  
 This marks the completion of the SoC
