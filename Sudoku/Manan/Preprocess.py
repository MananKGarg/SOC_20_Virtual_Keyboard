import cv2
import numpy as np

def Preprocess(image): # returns perspective transformed binary image of sudoku square in a 450*450 window

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # convert image to gray

    thg = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 71, 7)
    gblur = cv2.GaussianBlur(thg, (5, 5), 0)

    edges = cv2.Canny(gblur, 50, 150, apertureSize=3)  # Canny edge detection

    contours, heirarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # identigying contours

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 4000:
            # cv2.drawContours(img, cnt, -1,(0,0,255),3)
            approx = cv2.approxPolyDP(cnt, 20, True)
            cv2.drawContours(img, [approx], 0, (255, 0, 0), 5)
            # print(approx)

            pts = np.float32([approx[1][0], approx[0][0], approx[2][0], approx[3][0]])
            screenpts = np.float32([[0, 0], [449, 0], [0, 449], [449, 449]])

            matrix = cv2.getPerspectiveTransform(pts, screenpts)

            result = cv2.warpPerspective(thg, matrix, (450, 450))

    return(result)

# Testing the code
img = cv2.imread('sudoku.png')
res = Preprocess(img)
cv2.imshow('ans',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
