import numpy as np
import cv2
font = cv2.FONT_HERSHEY_SIMPLEX

# Create a black image
img = np.zeros((512,512,3), np.uint8)

cv2.putText(img,'testing text',(20,500), font, 1,(255,255,0),2,8)

cv2.imwrite('imWtext.png',img)
