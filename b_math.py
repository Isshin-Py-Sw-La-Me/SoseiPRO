#import cv2
#import numpy as np
#img = cv2.imread("./01.jpeg")
#img2 = cv2.imread("./02.png")
#px = img[100,100]
#print(px)
#print(img.shape)
#print(img2.shape)
#
#messi = cv2.imread("./messi5.jpg")
#ball = messi[280:330,300:400]
##messi[273:333,100:160] = ball
#cv2.imshow("messi",ball)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
import cv2
import numpy as np

img = cv2.imread("./messi5.jpg")
px = img[100,100]
print(px)
blue = img[100,100,0]
print(blue)

img[100,100] = [255,255,255]
print(img[100,100])
print(img.item(100,100,0))
print(img.shape)
print(img.size)
print(img.dtype)

ball = img[280:340,330:390]
img[273:333,100:160] = ball
#cv2.imshow("img",img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
b = img[:,:,0]
img[:,:,2] = 0

RED = [0,0,255]
img = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=RED)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
