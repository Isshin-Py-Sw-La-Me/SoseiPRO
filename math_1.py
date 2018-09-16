import cv2
import numpy as np

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y))
print(x+y)

cap = cv2.VideoCapture(0)

while(1):
    _,frame = cap.read()

    #Convert BGR to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
