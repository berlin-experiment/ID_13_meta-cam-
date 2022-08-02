import wave

test_audio = wave.open("/Users/staceykenny/Desktop/ID_13_meta-cam/red-death.wav")

test_audio_bytes = test_audio.readframes(-1)
print(test_audio_bytes)