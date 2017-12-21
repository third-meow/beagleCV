import cv2
import numpy as np

img = cv2.imread('start_img2.png',0)
ret,binThresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('BINARY',binThresh)
cv2.waitKey(0)

ret,invBinThresh = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('INV_BINARY',invBinThresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
