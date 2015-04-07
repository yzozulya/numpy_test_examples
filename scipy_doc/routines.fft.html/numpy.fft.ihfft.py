import numpy as np

spectrum = np.array([15, -4, 0, -1, 0, -4])
np.fft.ifft(spectrum)
np.fft.ihfft(spectrum)
