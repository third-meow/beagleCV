import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

cv2.rectangle(img,(100,100),(200,200),(255,255,0),3)

cv2.imwrite('rec.png',img)
