import numpy as np

freqs = np.fft.fftfreq(9, d=1. / 9).reshape(3, 3)
freqs
np.fft.ifftshift(np.fft.fftshift(freqs))
