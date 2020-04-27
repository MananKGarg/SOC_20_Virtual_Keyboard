import cv2
import numpy as np

def nothing(x):
    pass
# will not do anything, dummy function

cap = cv2.VideoCapture(0) # capturing frames usind webcam
#background = cv2.imread('saved_img.jpg', 1) ''' used this for a previously stored background image'''
ret, background = cap.read() # to read the initial background
#cv2.imshow('background', background)
cv2.namedWindow('Tracking') # trackbars to easily get the lower and upper hsv values of the cloth used
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing) # Lower hue
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing) # Lower saturation
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing) # Lower value
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing) # Upper hue
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing) # Upper saturation
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing) # Upper value
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.avi', fourcc, 20.0, (640,480)) # to save the written frame as output_video.avi
while True:
    _, frame = cap.read() # continuously reads the frame with webcam untill the while loop is not broken
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # converting the frame to hsv

    l_h  = cv2.getTrackbarPos('LH','Tracking')
    l_s  = cv2.getTrackbarPos('LS','Tracking')
    l_v  = cv2.getTrackbarPos('LV','Tracking')
    u_h  = cv2.getTrackbarPos('UH','Tracking')
    u_s  = cv2.getTrackbarPos('US','Tracking')
    u_v  = cv2.getTrackbarPos('UV','Tracking')

    l_b = np.array([l_h,l_s,l_v]) # array consisting the lower hsv values
    u_b = np.array([u_h,u_s,u_v]) # array consisting the upper hsv values

    mask = cv2.inRange(hsv, l_b, u_b) # to create a mask with only the cloth used in the frame using the lower and upper hsv values got from trackbars
    mask_inv = cv2.bitwise_not(mask) # to create a mask except the cloth area just by inversing the original mask
    res = cv2.bitwise_and(frame, frame, mask=mask_inv) # only shows the part expect the cloth in frame which is being captured by the camera
    res2 = cv2.bitwise_and(background, background, mask=mask) # this frame will show part of the captured background which is covered by the cloth
    res3 = cv2.bitwise_or(res,res2) # adding both frames with bitwise or operator
    #cv2.imshow('frame', frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    #cv2.imshow('res2', res2)

    out.write(res3) # writing the final frame on the output file

    cv2.imshow('res3', res3)

    #cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    # if q is pressed the loop breaks and the webcam stops capturing frames
    
cap.release()
out.release()
cv2.destroyAllWindows()
