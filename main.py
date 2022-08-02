import os
# from py_libs.cam import capture_image
# from py_libs.esp32_cam import capture_image
from py_libs.mac_cam import capture_image
from py_libs.detect import darknet_detect
from py_libs.audio import Dj

audio_output = Dj()

# gets our current working directory for metacam
PATH = os.getcwd() + "/darknetV2"

# to ensure we capture an image

try:
	while True:
		if os.path.exists(PATH+ "/data/test.jpg"):
			os.remove(PATH+ "/data/test.jpg")
			print("Previous prediction image removed")
			
		new_img = 1
		while new_img == 1:
			new_img = capture_image(PATH)
			
		people = darknet_detect(PATH)
		print("Detector detected "+ str(people)+" person(s)")
		
		audio_output.play(people)
		
except KeyboardInterrupt:
	print("Tschussies")
