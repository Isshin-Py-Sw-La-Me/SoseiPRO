import cv2
import numpy as np
img = cv2.imread("./01.jpeg")
img2 = cv2.imread("./02.png")
px = img[100,100]
print(px)
print(img.shape)
print(img2.shape)

messi = cv2.imread("./messi5.jpg")
ball = messi[280:330,300:400]
#messi[273:333,100:160] = ball
cv2.imshow("messi",ball)
cv2.waitKey(0)
cv2.destroyAllWindows()
