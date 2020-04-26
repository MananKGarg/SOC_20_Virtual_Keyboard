
~~~python
import numpy as np
import cv2
cap=cv2.VideoCapture(0)
ret,img=cap.read()                                                        #background image
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("outputfinal.avi",fourcc,20.0,(640,480))        #to store the video

def nothing(x):
    pass

cv2.namedWindow("Tracking")                                               #adding trackbars
cv2.createTrackbar("LH","Tracking",0,255,nothing)
cv2.createTrackbar("LS","Tracking",0,255,nothing)
cv2.createTrackbar("LV","Tracking",0,255,nothing)
cv2.createTrackbar("UH","Tracking",255,255,nothing)
cv2.createTrackbar("US","Tracking",255,255,nothing)
cv2.createTrackbar("UV","Tracking",255,255,nothing)

while(cap.isOpened()):
            ret,img1=cap.read()                                           #read each frames
            hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)                      #convert to hsv type



            l_h=cv2.getTrackbarPos("LH","Tracking")                       #get the corresponding value of track bars
            l_s=cv2.getTrackbarPos("LS","Tracking")
            l_v=cv2.getTrackbarPos("LV","Tracking")
            u_h=cv2.getTrackbarPos("UH","Tracking")
            u_s=cv2.getTrackbarPos("US","Tracking")
            u_v=cv2.getTrackbarPos("UV","Tracking")


            l_b=np.array([l_h,l_s,l_v])                                    #helps in making of mask
            u_b=np.array([u_h,u_s,u_v])                                    #helps in making of mask
          #  l_b=np.array([93,120,20])                                     #we can make mask manually also
          #  u_b=np.array([150,255,255])                                   #we can make mask manually also


            mask=cv2.inRange(hsv,l_b,u_b)                                  #making mask to get the invisible cloth area

            mask1 = cv2.bitwise_not(mask)                                  #making mask to get the remaining area in frame(excluding the invisible cloth area)
            res = cv2.bitwise_and(img1, img1, mask=mask1)                  #get the area of each frame excluding invisible cloth
            res1=cv2.bitwise_and(img,img,mask=mask)                        #get the area which is to be replaced in place of invisible cloth
            dst=cv2.add(res,res1)                                          #add both images ,gives final image
            cv2.imshow("dst",dst)
            out.write(dst)

            cv2.imshow("img",img)
            if cv2.waitKey(1) & 0xFF==ord('q'):                            #if key 'q' is pressed then loop break
                break


cap.release()
out.release()
cv2.destroyAllWindows()
~~~
