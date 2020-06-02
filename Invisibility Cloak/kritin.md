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
