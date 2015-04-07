from numpy import *
from numpy.fft import *

signal = array([-2., 8., -6., 4., 1., 0., 3., 5.])
fourier = fft(signal)
ifft(fourier)  # Inverse fourier transform
allclose(signal.astype(complex), ifft(fft(signal)))  # ifft(fft()) = original signal
N = len(fourier)
signal = empty(N, complex)
for k in range(N):  # equivalent but much slower
    signal[k] = sum(fourier * exp(+1j * 2 * pi * k * arange(N) / N)) / N
