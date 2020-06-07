# Code
---
``` python
import cv2
import copy
import numpy as np


def nothing(x):
    pass


def character(y_coor,x_coor,shape):

    a = y_coor//(shape[0]/6)
    b = x_coor//(shape[1]/10)

    keys = {}
    keys[(0,0)] = '!'; keys[(0,1)] = '@'; keys[(0,2)] = '#'; keys[(0,3)] = '$'
    keys[(0,4)] = '%'; keys[(0,5)] = '^'; keys[(0,6)] = '&'; keys[(0,7)] = '*'
    keys[(0,8)] = '('; keys[(0,9)] = ')'
    keys[(1,0)] = '1'; keys[(1,1)] = '2'; keys[(0,2)] = '3'; keys[(0,3)] = '4'
    keys[(1,4)] = '5'; keys[(1,5)] = '6'; keys[(1,6)] = '7'; keys[(1,7)] = '8'
    keys[(1,8)] = '9'; keys[(1,9)] = '0'
    keys[(2,0)] = 'q'; keys[(2,1)] = 'w'; keys[(2,2)] = 'e'; keys[(2,3)] = 'r'
    keys[(2,4)] = 't'; keys[(2,5)] = 'y'; keys[(2,6)] = 'u'; keys[(2,7)] = 'i' 
    keys[(2,8)] = 'o'; keys[(2,9)] = 'p'
    keys[(3,0)] = 'a'; keys[(3,1)] = 's'; keys[(3,2)] = 'd'; keys[(3,3)] = 'f'
    keys[(3,4)] = 'g'; keys[(3,5)] = 'h'; keys[(3,6)] = 'j'; keys[(3,7)] = 'k'
    keys[(3,8)] = 'l'; keys[(3,9)] = 'shift'
    keys[(4,0)] = 'z'; keys[(4,1)] = 'x'; keys[(4,2)] = 'c'; keys[(4,3)] = 'v'
    keys[(4,4)] = 'b'; keys[(4,5)] = 'n'; keys[(4,6)] = 'm'; keys[(4,7)] = ' '
    keys[(4,8)] = ' '; keys[(4,9)] = 'caps'
    keys[(5,0)] = ':'; keys[(5,1)] = ';'; keys[(5,2)] = '"'; keys[(5,3)] = "'"
    keys[(5,4)] = ','; keys[(5,5)] = '.'; keys[(5,6)] = '<'; keys[(5,7)] = '>'
    keys[(5,8)] = '/'; keys[(5,9)] = '?'

    return keys[(a,b)]



cap = cv2.VideoCapture('keyboard1.mp4')

_,frame1 = cap.read()
frame1 = cv2.resize(frame1,(int(frame1.shape[1]/2),int(frame1.shape[0]/2)))     #to make processing faster as video was taken by mobile(HQ)

orig = copy.deepcopy(frame1)        #making a copy to use the perpTransform & warpPersp variables in other frames
_,frame2 = cap.read()
frame2 = cv2.resize(frame2,(int(frame2.shape[1]/2),int(frame2.shape[0]/2)))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
final_out = cv2.VideoWriter('virtual_keyboard.avi',fourcc,20.0, (orig.shape[1],orig.shape[0]))

gray = cv2.cvtColor(orig,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(5,5),0)

thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,10)

contours,heirarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# for i in range(len(contours)):
#     if cv2.contourArea(contours[i]) > 40000  :
#         cv2.drawContours(orig,contours,16,(0,255,0),3)
#         print(i)
        
        # print(heirarchy[0][i],i)
#cv2.drawContours(orig,contours,27,(0,0,255),1)  #index mabe different for every video...hence has to be changed  
# cv2.imshow('framereqc',orig)
# cv2.imshow('thresh',thresh)

epsilon = 0.01*cv2.arcLength(contours[27],True)
approx = cv2.approxPolyDP(contours[27],epsilon,True)        #bounding rect to the keyboard

mask = np.zeros_like(gray)
out = np.zeros_like(gray)
cv2.drawContours(mask,[approx],0,255,-1)
out[mask == 255] = gray[mask == 255]                        #masking the keyboard

approx = np.reshape(approx,(4,2))
approx = approx.astype('float32')
out = out.astype('float32')

out_rect = np.array([[0,0],
                        [out.shape[0],0],           #persp transform on the keyboard warping it to the size of frame(resized)
                        [out.shape[0],out.shape[1]],
                        [0,out.shape[1]]],
                        dtype="float32")

persp = cv2.getPerspectiveTransform(approx,out_rect)
warp = cv2.warpPerspective(orig,persp,(out.shape[0],out.shape[1]))
warp = cv2.resize(warp,(out.shape[1],out.shape[0]))
# cv2.imshow('persp',warp)


counter = 0
caps = 0                
status = 0          #initializing variables to be used
y_coor = 0
x_coor = 0
string = ""
while(cap.isOpened):
    
    frame = copy.deepcopy(frame2)
    cv2.putText(frame,string,(0,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    final_out.write(frame)

    diff = cv2.absdiff(frame1,frame2)
    
    frame_warp = cv2.warpPerspective(diff,persp,(out.shape[0],out.shape[1]))
    frame_warp = cv2.resize(frame_warp,(out.shape[1],out.shape[0]))
    
    frame_gray = cv2.cvtColor(frame_warp,cv2.COLOR_BGR2GRAY)

    frame_blur = cv2.GaussianBlur(frame_gray,(3,3),0)

    frame_thresh = cv2.adaptiveThreshold(frame_blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,6)
    frame_thresh[0:10,:] = 255
    frame_thresh[350:360,:] = 255          # making the outer padding white
    frame_thresh[:,0:10] = 255
    frame_thresh[:,630:640] = 255

    frame_dilate = cv2.dilate(frame_thresh,(10,10),iterations=1)
    
    ratio = sum(sum(frame_thresh==0))/sum(sum(frame_thresh ==255))
    
    if ratio <= 0.0001:
        # print(counter)
        if counter==0 and status == 1:
            counter+=1
            temp = (diff_old == 0)
            for i in range(int(temp.shape[0])):
                for j in range(int(temp.shape[1])):
                    # print(temp[i][j])
                    # print(temp.shape,diff_old.shape,frame_thresh.shape)

                    if temp[i][j] == 1:
                        y_coor = i
                        x_coor = j
                        break
                else:
                    continue

                break
                
        elif counter < 10:
            counter+=1

        elif counter == 10:

            if (x_coor == 0 and y_coor == 0) or (x_coor == 10 and y_coor == 337):
                pass

            elif character(y_coor,x_coor,frame.shape) == 'caps' :
                caps = 1
            
            elif caps == 0:
                # print((y_coor,x_coor))
                char = character(y_coor,x_coor,frame.shape)
                # print(char)
                string = string + char

            else:
                char = character(y_coor,x_coor,frame.shape)
                # print(chr(ord(char) - 32))
                string = string + chr(ord(char) - 32)
            counter+=1

    else:
        counter = 0
        if status == 0:
            status = 1

    frame1 = copy.deepcopy(frame2)
    _,frame2 = cap.read()
    frame2 = cv2.resize(frame2,(int(frame2.shape[1]/2),int(frame2.shape[0]/2)))
    diff_old = copy.deepcopy(frame_thresh)
    
    k = cv2.waitKey(1)
    if k==27:
        break

cap.release()
final_out.release()
cv2.destroyAllWindows()

```

# Remarks

This code is not as versatile as an actual keyboard. Some of its limitations are-
* This code works only for one finger typing.
* Some parameters might have to be changed depending on the video.
* This code works with the Custom Keyboard provided by our mentor [here]()
* Typing must be slow and stable.

  
