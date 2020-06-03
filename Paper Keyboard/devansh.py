import urllib.request
import cv2
import numpy as np
import time


def point_of_interest(arr):#returns (x,y) coordinates of point of interest
    i = -1
    j = 0
    while (True):
        i = i + 1
        if (i == 1000):

            i = 0
            j = j + 1
        if (i == 0 and j == 600):
            return j, i
        if (arr[j][i] == 255):
            return j, i

def url_to_image(url):#convert url to image
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image


approx=0 # making some variables global
result0=0# making some variables global
text=" "
c=0#initialising a
s=0#initialising s
a=time.time()#initialising a
b=a+5#intialising b
devansh=34# making some variables global


def nothing(x):
    pass

url = "http://192.168.42.129:8080/shot.jpg"# for diffrent devices it may be diffrent


frame = url_to_image(url)
frame = cv2.resize(frame,(600,600))
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
adaptivethreshhold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 71, 7)
gblur = cv2.GaussianBlur(adaptivethreshhold, (5, 5), 0)
edges = cv2.Canny(gblur, 50, 150, apertureSize=3)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))
for contour in contours:
    area = cv2.contourArea(contour)
    if (area > 100000 and area < 200000):
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        cv2.drawContours(frame, [approx], 0, (255,0,0,), 5)
        pts1 = np.float32([[approx.ravel()[0], approx.ravel()[1]], [approx.ravel()[2], approx.ravel()[3]],
                           [approx.ravel()[4], approx.ravel()[5]], [approx.ravel()[6], approx.ravel()[7]]])
        pts2 = np.float32([[600, 600], [600, 0],[0, 0],[0, 600]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(frame, matrix, (600, 600))
        result0 = cv2.resize(result, (600, 600))


fresh=np.zeros((600,600,3),np.uint8)# black screen
devansh =np.zeros((600,600,3),np.uint8)#Screen on which text appears


while(True):

     frame = url_to_image(url)
     cv2.imshow('frame',frame)
     frame = cv2.resize(frame,(600,600))

     cv2.drawContours(frame, [approx], 0, (0), 5)

     pts1 = np.float32([[approx.ravel()[0], approx.ravel()[1]], [approx.ravel()[2], approx.ravel()[3]],
                       [approx.ravel()[4], approx.ravel()[5]], [approx.ravel()[6], approx.ravel()[7]]])
     pts2 = np.float32([ [600, 600], [600, 0],[0, 0],[0, 600]])

     matrix = cv2.getPerspectiveTransform(pts1, pts2)
     result = cv2.warpPerspective(frame, matrix, (600, 600))
     result1 = cv2.resize(result, (1000, 600))
     result2=result1.copy()
     result2=cv2.resize(result2,(600,600))
   #  cv2.imshow("result2",result2)
     hsv = cv2.cvtColor(result1, cv2.COLOR_BGR2HSV)
     l_b = np.array([0, 85, 0])  # helps in making of mask # values depends on user and on surrounding light
     u_b = np.array([255, 255, 255])

     mask = cv2.inRange(hsv, l_b, u_b)

     res1 = cv2.bitwise_and(result1, result1, mask=mask)

     gray_res1 = cv2.cvtColor(res1, cv2.COLOR_BGR2GRAY)
     _, thre_res1 = cv2.threshold(gray_res1, 50, 255, cv2.THRESH_BINARY)
     thre_res1 = cv2.erode(thre_res1, (10, 10), iterations=10)
     dilate = cv2.dilate(thre_res1, (10, 10), iterations=3)
     dilate=cv2.resize(dilate,(1000,600))
     cv2.imshow('dilate',dilate)
     cv2.imshow('result12',result0)

     cv2.imshow('devansh',devansh)
     cv2.waitKey(50)
     a=time.time()

     if b<=a:
         b=a+2.5 # takes a gap of 2.5 seconds in between taking two inputs
         x, y = point_of_interest(dilate)

         print('x: ',x,'  y: ',y)

         if (x <= 100 and x >= 30 and y <= 100 and y >= 30):
             if(c==0):
                 text = text + "!"
             else:
                 text = text + "!"
             print('!')
         elif (x <= 100 and x >= 0 and y <= 200 and y >= 100):
             if c==0:
                 text = text + "@"
             else:
                 text = text + "@"
             print('@')
         elif (x <= 100 and x >= 0 and y <= 300 and y >= 200):
             if c==0:
                 text = text + "#"
             else:
                 text = text + "#"
             print('#')
         elif (x <= 100 and x >= 0 and y <= 400 and y >= 300):
             if c==0:
                 text = text + "$"
             else:
                 text = text + "$"
             print('$')
         elif (x <= 100 and x >= 0 and y <= 500 and y >= 400):
            if c==0:
                text=text+"%"
            else:
                text = text + "%"
            print("%")
         elif (x <= 100 and x >= 0 and y <= 600 and y >= 500):
             if c==0:
                 text = text + "^"
             else:
                 text = text + "^"
             print("^")
         elif(x <= 100 and x >= 0 and y <= 700 and y >= 600):
             if c==0:
                 text = text + "&"
             else:
                 text = text + "&"
             print("&")
         elif (x <= 100 and x >= 0 and y <= 800 and y >= 700):
             if c==0:
                 text = text + "*"
             else:
                 text = text + "*"
             print("*")
         elif (x <= 100 and x >= 0 and y <= 900 and y >= 800):
             if c==0:
                 text = text + "("
             else:
                 text = text + "("
             print("(")
         elif (x <= 100 and x >= 0 and y <= 1000 and y >= 900):
             if c==0:
                 text = text + ")"
             else:
                 text = text + ")"
             print(")")
         elif (x <= 200 and x >= 0 and y <= 100 and y >= 30):
             if c==0:
                 text = text + "1"
             else:
                 text = text + "1"
             print("1")
         elif (x <= 200 and x >= 100 and y <= 200 and y >= 100):
             if c==0:
                 text = text + "2"
             else:
                 text = text + "2"
             print('2')
         elif (x <= 200 and x >= 100 and y <= 300 and y >= 200):
             if c==0:
                 text = text + "3"
             else:
                 text = text + "3"
             print('3')
         elif (x <= 200 and x >= 100 and y <= 400 and y >= 300):
             if c==0:
                 text = text + "4"
             else:
                 text = text + "4"
             print('4')
         elif (x <= 200 and x >= 100 and y <= 500 and y >= 400):
             if c==0:
                 text = text + "5"
             else:
                 text = text + "5"
             print('5')
         elif (x <= 200and x >= 100 and y <= 600 and y >= 500):
             if c==0:
                 text = text + "6"
             else:
                 text = text + "6"
             print('6')
         elif (x <= 200 and x >= 100 and y <= 700 and y >= 60):
             if c==0:
                 text = text + "7"
             else:
                 text = text + "7"
             print('7')
         elif (x <= 200 and x >= 100 and y <= 800 and y >= 700):
             if c==0:
                 text = text + "8"
             else:
                 text = text + "8"
             print('8')
         elif (x <= 200 and x >= 100 and y <= 900 and y >= 800):
             if c==0:
                 text = text + "9"
             else:
                 text = text + "9"
             print('9')
         elif (x <= 200 and x >= 100 and y <= 1000 and y >= 900):
             text = text + "0"
             print('0')
         elif (x <= 300 and x >= 200 and y <= 100 and y >= 30):
             if c==0:
                 text = text + "q"
                 print('q')
             else:
                 text = text + "Q"
                 print('Q')
         elif (x <= 300 and x >= 200 and y <= 200 and y >= 100):
             if c==0:
                 text = text + "w"
                 print('w')
             else:
                 text = text + "W"
                 print('W')
         elif (x <= 300 and x >= 200 and y <= 300 and y >= 200):
             if c==0:
                 text = text + "e"
                 print('e')
             else:
                 text = text + "E"
                 print('E')

         elif (x <= 300 and x >= 200 and y <= 400 and y >= 300):
             if c==0:
                 text = text + "r"
                 print('r')
             else:
                 text = text + "R"
                 print('R')

         elif (x <= 300 and x >= 200and y <= 500 and y >= 400):
             if c==0:
                 text = text + "t"
                 print('t')
             else:
                 text = text + "T"
                 print('T')

         elif (x <= 300 and x >= 200 and y <= 600 and y >= 500):
             if c==0:
                 text = text + "y"
                 print('y')
             else:
                 text = text + "Y"
                 print('Y')
         elif (x <= 300 and x >= 200 and y <= 700 and y >= 600):
             if c==0:
                 text = text + "u"
                 print('u')
             else:
                 text = text + "U"
                 print('U')
         elif (x <= 300 and x >= 200 and y <= 800 and y >= 700):
             if c==0:
                 text = text + "i"
                 print('i')
             else:
                 text = text + "I"
                 print('I')
         elif (x <= 300 and x >= 200 and y <= 900 and y >= 800):
             if c==0:
                 text = text + "o"
                 print('o')
             else:
                 text = text + "O"
                 print('O')
         elif (x <= 300 and x >= 200 and y <= 1000 and y >= 900):
             if c==0:
                 text = text + "p"
                 print('p')
             else:
                 text = text + "P"
                 print('P')
         elif (x <= 400 and x >= 300 and y <= 100 and y >= 30):
             if c==0:
                 text = text + "a"
                 print('a')
             else:
                 text = text + "A"
                 print('A')
         elif (x <= 400 and x >= 300 and y <= 200 and y >= 100):
             if c==0:
                 text = text + "s"
                 print('s')
             else:
                 text = text + "S"
                 print('S')
         elif (x <= 400 and x >= 300 and y <= 300 and y >= 200):
             if c==0:
                 text = text + "d"
                 print('d')
             else:
                 text = text + "D"
                 print('D')
         elif (x <= 400 and x >= 300 and y <= 400 and y >= 300):
             if c==0:
                 text = text + "f"
                 print('f')
             else:
                 text = text + "F"
                 print('F')
         elif (x <= 400 and x >= 300 and y <= 500 and y >= 400):
             if c==0:
                 text = text + "g"
                 print('g')
             else:
                 text = text + "G"
                 print('G')
         elif (x <= 400 and x >= 300 and y <= 600 and y >= 500):
             if c==0:
                 text = text + "h"
                 print('h')
             else:
                 text = text + "H"
                 print('H')
         elif (x <= 400 and x >= 300 and y <= 700 and y >= 600):
             if c==0:
                 text = text + "j"
                 print('j')
             else:
                 text = text + "J"
                 print('J')
         elif (x <= 400 and x >= 300 and y <= 800 and y >= 700):
             if c==0:
                 text = text + "k"
                 print('k')
             else:
                 text = text + "K"
                 print('K')
         elif (x <= 400 and x >= 300 and y <= 900 and y >= 800):
             if c==0:
                 text = text + "l"
                 print('l')
             else:
                 text = text + "L"
                 print('L')
         elif (x <= 400 and x >= 300 and y <= 1000 and y >= 900):
             n=len(text)
             text=text[:(n-1)]
             devansh=fresh.copy()
             print('BACK')
         elif (x <= 500 and x >= 400 and y <= 100 and y >= 30):
             if c==0:
                 text = text + "z"
                 print('z')
             else:
                 text = text + "Z"
                 print('Z')
         elif (x <= 500 and x >= 400 and y <= 200 and y >= 100):
             if c==0:
                 text = text + "x"
                 print('x')
             else:
                 text = text + "X"
                 print('X')
         elif (x <= 500 and x >= 400 and y <= 300 and y >= 200):
             if c==0:
                text = text +"c"
                print('c')
             else:
                 text = text + "C"
                 print('C')
         elif (x <= 500 and x >= 400 and y <= 400 and y >= 300):
             if c==0:
                 text = text + "v"
                 print('v')
             else:
                 text = text + "V"
                 print('V')
         elif (x <= 500 and x >= 400 and y <= 500 and y >= 400):
             if c==0:
                 text = text + "b"
                 print('b')
             else:
                 text = text + "B"
                 print('B')
         elif (x <= 500 and x >= 400 and y <= 600 and y >= 500):
             if c==0:
                 text = text + "n"
                 print('n')
             else:
                 text = text + "N"
                 print('N')
         elif (x <= 500 and x >= 400 and y <= 700 and y >= 600):
             if c==0:
                 text = text + "m"
                 print('m')
             else:
                 text = text + "M"
                 print('M')
         elif (x <= 500 and x >= 400 and y <= 800 and y >= 700):
             text = text + " "
             print('1')
         elif (x <= 500 and x >= 400 and y <= 900 and y >= 800):
             text = text + " "
             print('1')
         elif (x <= 500 and x >= 400 and y <= 1000 and y >= 900):
             text = text + ""
             if c==0:
                 c=1
             else:
                 c=0
             print("c:",c)
         elif (x <= 600 and x >= 500 and y <= 100 and y >= 30):
             text = text + ":"
             print('1')
         elif (x <= 600 and x >= 500 and y <= 200 and y >= 100):
             text = text + ";"
             print('1')
         elif (x <= 600 and x >= 500 and y <= 300 and y >= 200):
             text = text + "''"
             print('1')
         elif (x <= 600 and x >= 500 and y <= 400 and y >= 300):
             text = text + "'"
             print('1')
         elif (x <= 600 and x >= 500 and y <= 500 and y >= 400):
             text = text + ","
             print('1')
         elif (x <= 600 and x >= 500 and y <= 600 and y >= 500):
             text = text + "."
             print('1')
         elif (x <= 600 and x >= 500 and y <= 700 and y >= 600):
             text = text + "<"
             print('1')
         elif (x <= 600 and x >= 500 and y <= 800 and y >= 700):
             text = text + ">"
             print('1')
         elif (x <= 600 and x >= 500 and y <= 900 and y >= 800):
             text = text + "/"
             print('1')
         elif (x <= 600 and x >= 500 and y <= 1000 and y >= 900):
             text = text + "?"
             print('1')
         else:
             text = text + ""
             print("x: ",x,"y: ",y)
             print('1')
         font = cv2.FONT_HERSHEY_SIMPLEX
         text2="CAPS: ON"
         print("out")
         if c==1:
             print("in")
             devansh = cv2.putText(devansh,text2,(450,450),font,1 ,(0,255,255),2,cv2.LINE_AA)
             devansh = cv2.putText(devansh,text2,(450,950),font,1 ,(0,255,255),2,cv2.LINE_AA)
             devansh = cv2.putText(devansh, text, (100, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
         else:
             devansh=fresh.copy()
             print("in2")
             devansh = cv2.putText(devansh, text, (100, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)






