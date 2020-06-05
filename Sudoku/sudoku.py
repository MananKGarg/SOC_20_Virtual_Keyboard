import cv2
import numpy as np

img=cv2.imread('snew1.jpg',0)
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,71,7)       #thresholding of image
gblur=cv2.GaussianBlur(thresh,(5,5),0)                                                                #blurring of image
edges=cv2.Canny(gblur,50,150,apertureSize=3)                                                          #
#cv2.imshow('edges',edges)
contours,hierarchy=cv2.findContours(edges,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)                  #storing contours
for cnt in contours:
    area=cv2.contourArea(cnt)

    if area>400:
        approx=cv2.approxPolyDP(cnt,20,True)                                                          #storing max.area contour in a variable named approx.
        cv2.drawContours(img,[approx],0,(0,0,255),5)                                                  #drawing contours
        pts=np.float32([approx[1][0],approx[0][0],approx[2][0],approx[3][0]])
        screenpts=np.float32([[0,0],[251,0],[0,251],[251,251]])
        matrix=cv2.getPerspectiveTransform(pts,screenpts)                                             #performing perspective transform to get the desired size and its coordinates
        result=cv2.warpPerspective(thresh,matrix,(252,252))

print(result.shape)
a=0
k=0
erosion=np.zeros([81*28,28])                                                                          #
arr=np.zeros([81*28,28])                                                                              #declaring variables to store array of individual boxes
mask=np.zeros([81*28,28])                                                                             #
images=np.arange(81)
for i in range(0,252,28):
    for j in range(0,252,28):
        arr[a:a+28][:]=result[i:i+28,j:j+28]
        square=arr[a:a+28][:]
        _,mask[a:a+28][:]=cv2.threshold(square,0,255,cv2.THRESH_BINARY)                               #performing morphological operations to reduce noise in the individual boxes.
        kernal=np.ones((2,2),np.uint8)
        erosion=cv2.erode(mask,kernal,iterations=1)
        a+=28

print(result.size)
cv2.imshow('ans',result)                                                                              #displaying the perspective transformed image
cv2.imshow('res', arr[:28][:])                                                                        #displaying the first box of sudoku and its reduced noise image.
cv2.imshow('res1', mask[:28][:])
cv2.imshow('new',erosion[:28][:])
cv2.imwrite("roi.png", erosion[:28][:])                                                               #saving the first box of sudoku as an image

k=cv2.waitKey(0)
cv2.destroyAllWindows()
