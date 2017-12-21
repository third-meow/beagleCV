import cv2
import numpy as np

img = cv2.imread('compli_img2.png',0)
img = cv2.medianBlur(img,3)

meanImg = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
	cv2.THRESH_BINARY,11,2)

cv2.imshow('out',meanImg)

cv2.waitKey(0)
cv2.destroyAllWindows()
