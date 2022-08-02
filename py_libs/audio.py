import simpleaudio as sa
# Musik von <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=7015">Pixabay</a>
# frog Musik von <a href="/de/users/md_shakil-19198803/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=audio&amp;utm_content=10842">Md_Shakil</a> auf <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=10842">Pixabay</a>
# rain Musik von <a href="/de/users/fronbondi_skegs-23154649/?tab=audio&amp;utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=audio&amp;utm_content=10005">Fronbondi_Skegs</a> auf <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=10005">Pixabay</a>


class Layers:
	def __init__(self):
		self.sound1 = sa.WaveObject.from_wave_file("audio_files/sound3.wav")
		self.sound2 = sa.WaveObject.from_wave_file("audio_files/red-death.wav")
		self.sound3 = sa.WaveObject.from_wave_file("audio_files/sound3.wav")
		self.sound4 = sa.WaveObject.from_wave_file("audio_files/red-death.wav")
		


class Dj:
	def __init__(self):

		# self.sound1 = sa.WaveObject.from_wave_file("audio_files/sound3.wav")
		# self.sound2 = sa.WaveObject.from_wave_file("audio_files/red-death.wav")
		self.track1 = False
		self.track2 = False
		
	def play(self, people):
		if people == 0:
			if self.track1:
				self.track1.stop()
				self.track1 = False
			if self.track2:
				self.track2.stop()
				self.track2 = False

		if people == 1:
			if self.track1:
				if not self.track1.is_playing():
					self.track1 = self.sound1.play()
			else:
				self.track1 = self.sound1.play()
			if self.track2:
				self.track2.stop()
				self.track2 = False

		if people >= 2:
			if self.track1:
				self.track1.stop()
				self.track1 = False
			if self.track2:
				if not self.track2.is_playing():
					self.track2 = self.sound2.play()
			else:
				self.track2 = self.sound2.play()

		