Ensure that the end of your finger is painted black while using the keyboard.


```
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280,720))

#fourcc = cv2.VideoWriter_fourcc(*'MP4V')
#out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (1280,720))

newkey=np.array(['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','\n','Z','X','C','V','B','N','M',' ',' ','shift',':',';','"',"'",',','.','<','>','/','?'])
keys=np.reshape(newkey,(6,10))
caps = True
text=[" "]
key_threshold = 225
ret, t0 = cap.read()

t0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)


while True:

    ret, t1 = cap.read()
    temp=t1.copy()
    t1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(t1, t0)
    ret, result = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY)

    for i in range(0,6):
        for j in range(0,10):
             if cv2.countNonZero(result[100+(33*i):133+(33*i),190+(34*j):233+(34*j)])>key_threshold:
                  if (i,j)!=(5,9):
                      text.append(keys[i,j])
                  else:
                      caps=not caps


    pts1 = np.float32(([190,90], [500,100], [170,300], [500,300]))
    pts2 = np.float32(([0, 0], [1280, 0], [0, 720], [1280, 720]))
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    new = cv2.warpPerspective(temp, matrix, (1280, 720))


    cv2.imshow('Window', new)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(text)


cap.release()
cv2.destroyAllWindows()
```
