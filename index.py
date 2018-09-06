import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("./01.jpeg",0)
#cv2.imshow("image",img)
#cv2.imwrite("02.png",img)
#k = cv2.waitKey(0) & 0xFF
#if k == 27:
#    cv2.destroyAllWindows()
#elif k == ord("s"):
#    cv2.imwrite("mmm.png",img)
#    cv2.destroyAllWindows()
plt.imshow(img,cmap="gray",interpolation="bicubic")
plt.xticks([]),plt.yticks([])
plt.show()
