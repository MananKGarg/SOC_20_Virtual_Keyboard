```python
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

newkey=np.array(['!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','\n','Z','X','C','V','B','N','M',' ',' ','shift',':',';','"',"'",',','.','<','>','/','?'])
keys=np.reshape(newkey,(6,10))
caps = True
text=""
key_threshold = 10000
ret, t0 = cap.read()
t0 = cv2.cvtColor(t0, cv2.COLOR_BGR2GRAY)
area=0

while True:

    ret, t1 = cap.read()
    temp=t1.copy()
    t1 = cv2.cvtColor(t1, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(t1, t0)
    ret, result = cv2.threshold(diff, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(result, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)

    if area > 4000:

        approx = cv2.approxPolyDP(cnt, 20, True)
        cv2.drawContours(temp, [approx], 0, (255, 0, 0), 5)
        pts1 = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])
        pts2 = np.float32(([0, 0], [1280, 0], [0, 720], [1280, 720]))
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        new = cv2.warpPerspective(temp, matrix, (1280, 720))

        for i in range(0, 6):
          for j in range(0, 10):
            if cv2.countNonZero(new[(120 * i):120 + (120 * i), (127 * j):127 + (127 * j)]) < key_threshold:
                if (i, j) != (4, 9):
                    text.append(keys[i, j])
                else:
                    caps = not caps

        cv2.imshow('Window', new)


        if cv2.waitKey(1) & 0xFF == ord('q'):
          break

    print(text)


cap.release()
cv2.destroyAllWindows()
