Note - The code takes input with a time gap of 2.5 seconds.

```python
import requests
import cv2
import numpy as np
import time

'''
def nothing(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar('LH', 'Tracking', 0, 255, nothing) # Lower hue
cv2.createTrackbar('LS', 'Tracking', 0, 255, nothing) # Lower saturation
cv2.createTrackbar('LV', 'Tracking', 0, 255, nothing) # Lower value
cv2.createTrackbar('UH', 'Tracking', 255, 255, nothing) # Upper hue
cv2.createTrackbar('US', 'Tracking', 255, 255, nothing) # Upper saturation
cv2.createTrackbar('UV', 'Tracking', 255, 255, nothing) # Upper value
'''

url = "http://192.168.43.1:8080/shot.jpg"

a= time.time()
b = a+5
text = ""
y_line = 50
output = np.zeros((311,523,3),np.uint8)
final_screen = np.zeros((622, 523, 3),np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX

key_resp = requests.get(url)
key_arr = np.array(bytearray(key_resp.content), dtype=np.uint8)
key = cv2.imdecode(key_arr, -1)
key = cv2.resize(key, (960,540))

gray_key = cv2.cvtColor(key, cv2.COLOR_BGR2GRAY)  # convert image to gray
thg_key = cv2.adaptiveThreshold(gray_key, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 71, 7)
gblur_key = cv2.GaussianBlur(thg_key, (5, 5), 0)
edges_key = cv2.Canny(gblur_key, 50, 150, apertureSize=3)  # Canny edge detection
contours, heirarchy = cv2.findContours(edges_key, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # identifying contours
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 150000 :  # To detect the biggest square

        approx = cv2.approxPolyDP(cnt, 20, True)
        cv2.drawContours(key, [approx], 0, (255, 0, 0), 5)  # Drawing blue countour over approximated square

        pts = np.float32(
            [approx[0][0], approx[3][0], approx[1][0], approx[2][0]])  # Top-left, Top-right, Bottom-left, Bottom-right
        screenpts = np.float32([[0, 0], [522, 0], [0, 310], [522, 310]])

        matrix = cv2.getPerspectiveTransform(pts, screenpts)
        result = cv2.warpPerspective(thg_key, matrix, (523, 311))

#cv2.imshow("keyboard", result)
#print(pts)
#print(screenpts)

shifted = False

#fourcc = cv2.VideoWriter_fourcc(*'XVID') # or fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
#out = cv2.VideoWriter('virtual_keyboard.avi', fourcc, 20.0, (523,622))

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = cv2.resize(img, (960,540))

    kb_per = cv2.getPerspectiveTransform(pts, screenpts)
    kb_live = cv2.warpPerspective(img, kb_per, (523, 311))

    if (shifted == True):
        cv2.circle(kb_live, (509, 226), 4, (0, 255, 0), -1)


    hsv = cv2.cvtColor(kb_live, cv2.COLOR_BGR2HSV)

    '''
    l_h = cv2.getTrackbarPos('LH', 'Tracking')
    l_s = cv2.getTrackbarPos('LS', 'Tracking')
    l_v = cv2.getTrackbarPos('LV', 'Tracking')
    u_h = cv2.getTrackbarPos('UH', 'Tracking')
    u_s = cv2.getTrackbarPos('US', 'Tracking')
    u_v = cv2.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    '''

    l_b = np.array([0, 50, 50])
    u_b = np.array([33, 255, 255])
    mask = cv2.inRange(hsv, l_b, u_b)
    contours, heirarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # identifying contours
    if (len(contours) !=0):
        for cn in contours:
            area1 = cv2.contourArea(cn)
            if area1 > 100:
                c = max(contours, key=cv2.contourArea)
                #cv2.drawContours(kb_live, c, -1, (0, 255, 0), 3)
                extTop = tuple(c[c[:, :, 1].argmin()][0])
                #print(extTop)
                #cv2.circle(kb_live, extTop, 8, (255, 0, 0), -1)



        #print(extTop)
        x = extTop[0]
        y = extTop[1]
        a = time.time()

        if (b<=a):
            b = a+2

            if (x >469.8 and x < 522 and y > 206.64 and y < 258.3):
                if (shifted==True):
                    shifted = False
                    print('shifted is false')

                else:
                    shifted = True
                    print('shifted is true')
                    cv2.circle(kb_live, (509, 226), 8, (0, 255, 0), -1)

            elif(x>0 and x<52.2 and y>0 and y<51.66):
                text = text + '!'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 52.2 and x < 104.4 and y > 0 and y < 51.66):
                text = text + '@'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 104.4 and x < 156.6 and y > 0 and y < 51.66):
                text = text + '#'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 156.6 and x < 208.8 and y > 0 and y < 51.66):
                text = text + '$'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 208.8 and x < 261 and y > 0 and y < 51.66):
                text = text + '%'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 261 and x < 313.2 and y > 0 and y < 51.66):
                text = text + '^'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 313.2 and x < 365.4 and y > 0 and y < 51.66):
                text = text + '&'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 365.4 and x < 417.6 and y > 0 and y < 51.66):
                text = text + '*'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 417.6 and x < 469.8 and y > 0 and y < 51.66):
                text = text + '('
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 469.8 and x < 522 and y > 0 and y < 51.66):
                text = text + ')'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 0 and x < 52.2 and y > 51.66 and y < 103.32):
                text = text + '1'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 52.2 and x < 104.4 and y > 51.66 and y < 103.32):
                text = text + '2'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 104.4 and x < 156.6 and y > 51.66 and y < 103.32):
                text = text + '3'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 156.6 and x < 208.8 and y > 51.66 and y < 103.32):
                text = text + '4'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 208.8 and x < 261 and y > 51.66 and y < 103.32):
                text = text + '5'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 261 and x < 313.2 and y > 51.66 and y < 103.32):
                text = text + '6'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 313.2 and x < 365.4 and y > 51.66 and y < 103.32):
                text = text + '7'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 365.4 and x < 417.6 and y > 51.66 and y < 103.32):
                text = text + '8'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 417.6 and x < 469.8 and y > 51.66 and y < 103.32):
                text = text + '9'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 469.8 and x < 522 and y > 51.66 and y < 103.32):
                text = text + '0'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 0 and x < 52.2 and y > 258.3 and y < 310):
                text = text + ':'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 52.2 and x < 104.4 and y > 258.3 and y < 310):
                text = text + ';'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 104.4 and x < 156.6 and y > 258.3 and y < 310):
                text = text + '"'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 156.6 and x < 208.8 and y > 258.3 and y < 310):
                text = text + "'"
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 208.8 and x < 261 and y > 258.3 and y < 310):
                text = text + ','
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 261 and x < 313.2 and y > 258.3 and y < 310):
                text = text + '.'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 313.2 and x < 365.4 and y > 258.3 and y < 310):
                text = text + '<'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 365.4 and x < 417.6 and y > 258.3 and y < 310):
                text = text + '>'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 417.6 and x < 469.8 and y > 258.3 and y < 310):
                text = text + '/'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 469.8 and x < 522 and y > 258.3 and y < 310):
                text = text + '?'
                print(text)
                output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 0 and x < 52.2 and y > 103.32 and y < 154.98):
                if (shifted==True):
                    text = text + 'Q'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'q'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 52.2 and x < 104.4 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'W'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'w'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 104.4 and x < 156.6 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'E'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'e'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 156.6 and x < 208.8 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'R'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'r'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 208.8 and x < 261 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'T'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 't'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 261 and x < 313.2 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'Y'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'y'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 313.2 and x < 365.4 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'U'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'u'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 365.4 and x < 417.6 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'I'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'i'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 417.6 and x < 469.8 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'O'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'o'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 469.8 and x < 522 and y > 103.32 and y < 154.98):
                if (shifted == True):
                    text = text + 'P'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'p'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 0 and x < 52.2 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'A'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'a'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 52.2 and x < 104.4 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'S'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 's'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 104.4 and x < 156.6 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'D'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'd'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 156.6 and x < 208.8 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'F'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'f'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 208.8 and x < 261 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'G'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'g'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 261 and x < 313.2 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'H'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'h'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 313.2 and x < 365.4 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'J'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'j'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 365.4 and x < 417.6 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'K'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'k'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 417.6 and x < 469.8 and y > 154.98 and y < 206.64):
                if (shifted == True):
                    text = text + 'L'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'l'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 469.8 and x < 522 and y > 154.98 and y < 206.64):
                y_line = y_line + 30
                text = ""
                print("Enter is pressed")

            elif (x > 0 and x < 52.2 and y > 206.64 and y < 258.3):
                if (shifted == True):
                    text = text + 'Z'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'z'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 52.2 and x < 104.4 and y > 206.64 and y < 258.3):
                if (shifted == True):
                    text = text + 'X'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'x'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 104.4 and x < 156.6 and y > 206.64 and y < 258.3):
                if (shifted == True):
                    text = text + 'C'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'c'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 156.6 and x < 208.8 and y > 206.64 and y < 258.3):
                if (shifted == True):
                    text = text + 'V'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'v'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 208.8 and x < 261 and y > 206.64 and y < 258.3):
                if (shifted == True):
                    text = text + 'B'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'b'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 261 and x < 313.2 and y > 206.64 and y < 258.3):
                if (shifted == True):
                    text = text + 'N'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'n'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)



            elif (x > 313.2 and x < 365.4 and y > 206.64 and y < 258.3):
                if (shifted == True):
                    text = text + 'M'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)


                else:
                    text = text + 'm'
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)

            elif (x > 365.4 and x < 469.8 and y > 206.64 and y < 258.3):
                    text = text + ' '
                    print(text)
                    output = cv2.putText(output, text, (10, y_line), font, 0.75, (255, 255, 255), 2, cv2.LINE_AA)

    final_screen[:311,:] = output[:,:]
    final_screen[311:,:] = kb_live[:,:]
    #cv2.imshow('keyboard live', kb_live)
    #cv2.imshow('mask',mask)
    #cv2.imshow('output', output)
    #out.write(final_screen)
    cv2.imshow('final_screen',final_screen)

    if cv2.waitKey(1) == 27:
        break

#out.release()
cv2.destroyAllWindows()

```
