import time
from threading import Thread
import cv2
import imutils

class FPS:
	def __init__(self):
		self._start = None
		self._end = None
		self._numFrames = 0

	def start(self):
		self._start = time.time()
		return self

	def stop(self):
		self._end = time.time()

	def update(self):
		self._numFrames += 1

	def elapsed(self):
		return self._end - self._start

	def fps(self):
		return self._numFrames / self.elapsed()

class CamStream:
	def __init__(self, src=0):
		self.stream = cv2.VideoCapture(src)
		(self.grabbed, self.frame) = self.stream.read()

		self.stopped = False

	def start(self):
		Thread(target=self.update, args=()).start()
		return self

	def update(self):
		while True:
			if self.stopped:
				return
		(self.grabbed, self.frame) = self.stream.read()

	def read(self):
		return self.frame

	def stop(self):
		self.stopped = True



vs = CamStream().start()
fps = FPS().start()
usr_frames = input('Frames: ')
while fps._numFrames < usr_frames:
	frame = vs.read()
	fps.update()

fps.stop()
print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

cv2.destroyAllWindows()
vs.stop()
