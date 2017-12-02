
import cv2

ramp_frames = 30

camera = cv2.VideoCapture(0)

def get_image():
	retval, im = camera.read()
	return im

for i in xrange(ramp_frames):
	temp = get_image()
print('Taking image...')

camera_capture = get_image()
file = input('File Name: ')

cv2.imwrite(file, camera_capture)

del(camera)
