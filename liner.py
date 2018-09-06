import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
img = cv2.line(img,(510,0),(511,511),(255,0,0),5)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
img = cv2.rectangle(img,(0,384),(128,510),(255,0,0),5)
img = cv2.circle(img,(447,63),63,(0,0,255),1)
img = cv2.circle(img,(447,63),45,(0,0,255),-1)
cv2.imshow("liner",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
