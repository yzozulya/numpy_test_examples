import numpy as np

from numpy.fft import fft, fftshift

A = fft(window, 2048) / 25.5
A
freq = np.linspace(-0.5, 0.5, len(A))
