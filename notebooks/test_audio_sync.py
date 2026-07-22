import librosa
import numpy as np

y1, sr = librosa.load('data/staged/phone1_audio.wav', sr=None)
y2, _ = librosa.load('data/staged/phone2_audio.wav', sr=sr)

corr = np.correlate(y1, y2, mode='full')
offset_samples = np.argmax(corr) - (len(y2) - 1)
offset_seconds = offset_samples / sr
print(f"Offset: {offset_seconds:.3f} seconds")