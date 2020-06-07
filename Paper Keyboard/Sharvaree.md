## Paper Keyboard Implementation-

### Steps performed in the code-
1. Reading of video.
2. Performing perspective transform and getting max.area which is assumed to be of keyboard.
3. reducing noise.
3. Background Subtraction and thresholding hand's frame.
4. Detecting topmost tip of finger.
5. Detecting whether the key is presssed or not.
6. Checking whether the key is capslock or not
7. Typing text on frame according to lower_case or upper_case.

The Code is as follows:
```python
import cv2
import numpy as np
from datetime import datetime as dt

dict=np.array([['!','@','#','$','%','^','&','*','(',')'],
               ['1','2','3','4','5','6','7','8','9','0'],
               ['q','w','e','r','t','y','u','i','o','p'],
               ['a','s','d','f','g','h','j','k','l',' '],
               ['z','x','c','v','b','n','m',' ',' ',' '],
               [':',';','"','`',',','.','<','>','/','?']])

cap=cv2.VideoCapture('keyboard2.mp4')

fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False)
current=dt.now()
initial=dt.now()
x,y=0,0
cx,cy=0,0
cx_now,cy_now=0,0
i,j=0,0
key_pressed=False
n=30

def get_key(top):
    #global i,j

    tip = tuple(top[top[:, :, 1].argmin()][0])
    x, y = tip
    i = x // 100
    j = y // 100
    return i,j

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 199, 6)
    gblur = cv2.GaussianBlur(thresh, (5, 5), 0)
    edges = cv2.Canny(gblur, 50, 150, apertureSize=3)

    pts1=np.float32([[23,51],[434,51],[27,299],[434,287]])
    pts2=np.float32([[0,0],[999,0],[0,599],[999,599]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    result = cv2.warpPerspective(thresh, matrix, (1000, 600))

    _,mask=cv2.threshold(result,0,255,cv2.THRESH_BINARY)
    kernel=np.ones((5,5),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=2)

    handmask = fgbg.apply(erosion)

    contours,hierarchy=cv2.findContours(handmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    maxarea=0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if(area>=maxarea):
            maxarea=area
            desired_contour=cnt

    cx_now,cy_now=cx,cy
    cx, cy = get_key(desired_contour)
    if (cx,cy)!=(cx_now,cy_now):
        initial=dt.now()
    current=dt.now()
    diff=current-initial
    if diff.microseconds>=600000:
        initial=dt.now()
        key_pressed=True

    if key_pressed==True:
        key_value=dict[cy][cx]
        n = n + 20
        frame=cv2.putText(frame,''.join(key_value),(n,25),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)


    cv2.imshow('frames',frame)
    cv2.imshow('backsub',handmask)
    cv2.imshow('final',frame)

    k = cv2.waitKey(30)
    if k == 'q' or k == 27:
        break

cap.release()
cv2.destroyAllWindows()

```

The code with introduction of capslock key is as follows-
```python
import cv2
import numpy as np
import time
from datetime import datetime

lower_case={0:'!',1:'@',2:'#',3:'$',4:'%',5:'^',6:'&',7:'*',8:'(',9:')',                                              
            10:'1',11:'2',12:'3',13:'4',14:'5',15:'6',16:'7',17:'8',18:'9',19:'0',
            20:'q',21:'w',22:'e',23:'r',24:'t',25:'y',26:'u',27:'i',28:'o',29:'p',
            30:'a',31:'s',32:'d',33:'f',34:'g',35:'h',36:'j',37:'k',38:'l',39:'shift',                                 #Declaring dictionary of lower case characters 
            40:'z',41:'x',42:'c',43:'v',44:'b',45:'n',46:'m',47:' ',48:' ',49:'caps',
            50:':',51:';',52:'"',53:'`',54:',',55:'.',56:'<',57:'>',58:'/',59:'?'}

upper_case={0:'!',1:'@',2:'#',3:'$',4:'%',5:'^',6:'&',7:'*',8:'(',9:')',
            10:'1',11:'2',12:'3',13:'4',14:'5',15:'6',16:'7',17:'8',18:'9',19:'0',
            20:'Q',21:'W',22:'E',23:'R',24:'T',25:'Y',26:'U',27:'I',28:'O',29:'P',
            30:'A',31:'S',32:'D',33:'F',34:'G',35:'H',36:'J',37:'K',38:'L',39:'shift',                                 #Declaring dictionary of lower case characters 
            40:'Z',41:'X',42:'C',43:'V',44:'B',45:'N',46:'M',47:' ',48:' ',49:'caps',
            50:':',51:';',52:'"',53:'`',54:',',55:'.',56:'<',57:'>',58:'/',59:'?'}

i,j=0,0                                                                                                                #Initializing the variables
o_i,o_j=0,0                                                                                                            #old and new coordinates of image array
caps=False                                                                                                             #initially assuming caps key to be off
current=datetime.now()                                                                                                 #initializing current and 
initial=datetime.now()                                                                                                 #initial time

fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=False)

def get_perspective_transform(frame):                                                                                  
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)                                                                        #converting into grayscale image
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 71, 7)            #performin thresholding oon small regions
    gblur = cv2.GaussianBlur(thresh, (5, 5), 0)                                                                        #blurring the image
    edges = cv2.Canny(gblur, 50, 150, apertureSize=3)                                                                  #canny edge detection
    contours,hierarchy=cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)                             #determining contours
    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 4000:
            approx = cv2.approxPolyDP(cnt, 20, True)                                                                   #defining polygon with max.area
            #cv2.drawContours(img, [approx], 0, (0, 0, 255), 5)
            pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])                                 # 
            screenpts = np.float32([[0, 0], [499, 0], [0, 299], [499, 299]])                                           #performing pespective transform
            matrix = cv2.getPerspectiveTransform(pts, screenpts)                                                       #
            result = cv2.warpPerspective(thresh, matrix, (500, 300))                                                   #
    return result

def background_subtraction(v_k_1):
    fg_mask=fgbg.apply(v_k_1)                                                                                          #seperating foreground mask 
    return fg_mask

def reduce_noise(b_g_s):
    kernel=np.ones((3,3),np.uint8)                                                                                     #
    fg_mask1 = cv2.erode(b_g_s, kernel, iterations=1)                                                                  #removing unwanted pixels
    return fg_mask1                                                                                                    #

def max_contour(thresh1):
    maxArea=0                                                                                                          #
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)                            #
    for cnt in contours:                                                                                               #
        area=cv2.contourArea(cnt)                                                                                      #finding contour with max area
        if area>maxArea:                                                                                               #of threshed hand
            maxArea=area                                                                                               #
            maxContour=cnt                                                                                             #
    return maxContour

def get_key(cont):   
    a=cv2.contourArea(cont)                                                                                            #
    if(a>500 | a<10000):                                                                                               #finding topmost point on finger
        top=tuple(a[a[:,:,1].argmin()][0])                                                                             #this point will be with min. y coordinate 
        (x_f,y_f)=top                                                                                                  #of threshed hand.
        i=x_f//50                                                                                                      #
        j=y_f//50                                                                                                      #
        #k=i*10+j
        return (i,j)

def decide_case(cx,cy):                                                                                                #checking if caps is pressed
    global caps
    q=caps
    if (cx,cy)==(9,4) & caps==True:                                                                                                  #
        q= not caps                                                                                                      #caps is ON
    if (cx,cy)==(9,4) & caps==False:                                                                                                              #
        q=not caps                                                                                                     #caps is OFF
    return q

def detect_press(img):
    global current,initial,o_i,o_j,i,j                                                                                 #
    o_i,o_j=i,j                                                                                                        #
    i,j=get_key(img)                                                                                                   #obtaining coordinates of topmost finger point
    if (o_i,o_j)!=(i,j):                                                                                               #
        initial=datetime.now()                                                                                         #storing initial frame time
    current=datetime.now()                                                                                             #storing current frame time
    diff=current-initial                                                                                               #calculating difference between current and initial frame
    if diff.microseconds>=300000:
        #new_text(lower_case1[j,i])
        d=decide_case(i,j)
        return d

cap=cv2.VideoCapture('keyboard.mp4')                                                                                   #capturing video

time.sleep(1)

while True:
    ret,frame=cap.read()
    #img = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    v_k_1=get_perspective_transform(frame)                                                                             #
    b_g_s=background_subtraction(v_k_1)                                                                                #
    r_n=reduce_noise(b_g_s)                                                                                            #performing operations step by step
    fg_mask2=cv2.bitwise_and(b_g_s,b_g_s,mask=r_n)                                                                     #as given above the code
    grayMask = cv2.cvtColor(fg_mask2, cv2.COLOR_BGR2GRAY)                                                              #
    ret, thresh = cv2.threshold(grayMask, 40, 255, 0)                                                                  #
    max_area=max_contour(thresh)
    if max_area is not None:
        c=detect_press(max_area)
    k=10*j+i                                                                                                           #calculting key to get the value in the dictionary
    if c==True:
        text=upper_case[k]                                                                                             #obtaining keyvalue
        frame=cv2.circle(frame,(429,241),5,(255,0,0),-1)                                                               #drawing circle indicating caps key is ON
        frame=cv2.putText(frame,''.join(text),(30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)                     #writing text in upper case
    else:
        text=lower_case[k]
        frame=cv2.putText(frame,''.join(text),(30,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)                          #writing text in lower case
    cv2.imshow('frame',frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

```
### Some assumptions and precautions to be taken care of-

1. while taking video camera should not be disturbed.
2. Here,max contour area is assumed to be of keyboard.
3. Only one finger is used at a time.
