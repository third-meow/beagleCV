import numpy
import cv2

camra_port = 0
cap = cv2.VideoCapture(camra_port)

while(True):
	ret,frame = cap.read()     				# Capture frame-by-frame
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)		# Our operations on the frame come here
	cv2.imshow('Live Feed',frame)		    		# Display the resulting frame

	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
cap.release()
cv2.destroyAllWindows()
