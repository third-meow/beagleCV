import cv2
import numpy as np

C920 = cv2.VideoCapture(0)
try:
	while True:
		notneeded,frame = C920.read()	    		#capture a  frame

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 	#convert to HSV

		lower_green = np.array([80,80,80])		#define green range
		upper_green = np.array([90,240,240])

		mask = cv2.inRange(hsv, lower_green, upper_green)	#only look at the green

		res = cv2.bitwise_and(frame,frame, mask= mask)		#add images together

		cv2.imshow('result',res) 				#print mask image to screen
		vv = cv2.waitKey(1)

except KeyboardInterrupt:
	cv2.destroyAllWindows()
	del(C920)
	print('Goodbye')
