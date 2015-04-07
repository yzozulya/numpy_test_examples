import numpy as np

signal = np.array([1, 2, 3, 4, 3, 2])
np.fft.fft(signal)
np.fft.hfft(signal[:4])  # Input first half of signal
np.fft.hfft(signal, 6)  # Input entire signal and truncate
signal = np.array([[1, 1.j], [-1.j, 2]])
np.conj(signal.T) - signal  # check Hermitian symmetry
freq_spectrum = np.fft.hfft(signal)
freq_spectrum
