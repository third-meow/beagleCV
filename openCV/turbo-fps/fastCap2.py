import time
from threading import Thread
import cv2
import imutils
import sys
sys.path.insert(0,'/home/jds/src/my_py/mods')
from cvThread import CamStream

vs = CamStream().start()
usr_frames = input('Frames: ')
for i in range(usr_frames):
	frame = vs.read()
	cv2.imshow('result',frame)
	kk = cv2.waitKey(20)
cv2.destroyAllWindows()
vs.stop()
