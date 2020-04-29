# Invisibility Cloak
## Concept
- The main idea is to replace the area covered by a *single coloured* cloak, with a memory image(Previously known background).
- To detect the cloak, we use HSV instead of RGB.Reason:
    * RGB Color values are sensitive to lighting conditions.
    * HSV Color system is quite good when it comes to color detection as it takes into account the intensity of light.
- For this, we use image segmentation
- The Process is as follows:
    1. Capture the background without the cloak in it
    2. Detect the area covered by cloak using HSV color scheme
    3. Segment out the area by defining a mask
    4. Add the same area but from the previously captured background

```python
import cv2
import numpy as np

# Objects for reading and writing videos
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# Pre-magic setup

def nothing():
    pass


cv2.namedWindow('Color')                                # Declaring window for trackbar
cv2.createTrackbar('LHue', 'Color', 0, 180, nothing)    # Trackbar of lower hue
cv2.createTrackbar('LSat', 'Color', 0, 255, nothing)    # Trackbar of lower saturation
cv2.createTrackbar('LVal', 'Color', 0, 255, nothing)    # Trackbar of lower value
cv2.createTrackbar('UHue', 'Color', 0, 180,nothing)     # Trackbar of upper hue

background = 0

# Capture the background to be added instead of cloth
for i in range(60):
    ret, background = cap.read()
    background = np.flip(backgroung, axis=1)            # By default camera captures laterally inverted image

while cap.isOpened:
    ret, frame = cap.read()
    frame = np.flip(frame, axis=1)

    # HSV is based on light intensity, so it'll capture the cloak better as compared to RGB
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Limits for the color of cloak
    lHue = cv2.getTrackbarPos('LHue', 'Color')
    lSat = cv2.getTrackbarPos('LSat', 'Color')
    lVal = cv2.getTrackbarPos('LVal', 'Color')
    uHue = cv2.getTrackbarPos('UHue', 'Color')
    lowColor = np.array([lHue,lSat,lVal])
    upColor = np.array([uHue,255,255])
    cloak = cv2.inRange(hsv, lowColor, upColor)                   # Mask to capture the area of cloak

    # To smoothen the area captured by cloak in webcam
    cloak = cv2.morphologyEx(cloak, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    cloak  = cv2.morphologyEx(cloak, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    non_cloak = cv2.bitwise_not(cloak)                             # Mask to capture area not covered by cloak

    non_cloak = cv2.bitwise_and(frame, frame, mask=non_cloak)      # Area not covered by cloak
    cloak = cv2.bitwise_and(background, background, mask=cloak)    # Area covered by cloak

    frame = cv2.add(cloak, non_cloak)                              # Adding both the areas for the magical effect
    cv2.imshow('Invisibility Cloak', frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
         break

cap.release()
out.release()
cv2.destroyAllWindows()
```
