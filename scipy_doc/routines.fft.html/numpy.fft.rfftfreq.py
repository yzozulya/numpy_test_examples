import numpy as np

signal = np.array([-2, 8, 6, 4, 1, 0, 3, 5, -3, 4], dtype=float)
fourier = np.fft.rfft(signal)
n = signal.size
sample_rate = 100
freq = np.fft.fftfreq(n, d=1. / sample_rate)
freq
freq = np.fft.rfftfreq(n, d=1. / sample_rate)
freq
