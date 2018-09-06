import numpy as np
import cv2

img = cv2.imread('1.jpg',1)
cv2.imshow('test',img)
k = cv2.waitKey(0) & 0xFF
if k == 27: #wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): #wait for 's'key to save and exit
    cv2.imwrite('save.png',img)
    cv2.destroyAllWindows