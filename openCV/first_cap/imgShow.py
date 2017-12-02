import numpy
import cv2

img = cv2.imread('first_cap1.png',1)
cv2.imshow('XD',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#cv2.imwrite('first_cap_grayscale.png',img)
