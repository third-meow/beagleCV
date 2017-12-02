import numpy as np
import cv2

path = input('File: ')

img = cv2.imread(path,1)
cv2.imshow(path,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
