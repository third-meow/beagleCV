import sys
sys.path.insert(0, "/home/jds/src/my_py/mods")
import cv2
import numpy as np
from cvThread import CamStream
from cvThread import FPS


try:
	fps = FPS().start()
	C920 = CamStream().start()
	while True:
		frame = C920.read()	    		#capture a  frame
		print('life')
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 	#convert to HSV

		lower_green = np.array([80,80,80])		#define green range
		upper_green = np.array([90,240,240])

		mask = cv2.inRange(hsv, lower_green, upper_green)	#only look at the green

		#res = cv2.bitwise_and(frame,frame, mask= mask)		#add images together

		cv2.imshow('result',frame) 				#print mask image to screen
		vv = cv2.waitKey(1)

		fps.update()

except KeyboardInterrupt:
	fps.stop()
	cv2.destroyAllWindows()
	print('\n'+str(fps.elapsed())+'Time')
	print(str(fps.fps())+'FPS')
	C920.stop()
