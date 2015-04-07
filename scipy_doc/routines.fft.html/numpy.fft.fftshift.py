import numpy as np

freqs = np.fft.fftfreq(10, 0.1)
freqs
np.fft.fftshift(freqs)
freqs = np.fft.fftfreq(9, d=1. / 9).reshape(3, 3)
freqs
np.fft.fftshift(freqs, axes=(1,))
