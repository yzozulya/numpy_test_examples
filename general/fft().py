from numpy import *
from numpy.fft import *

signal = array([-2., 8., -6., 4., 1., 0., 3., 5.])  # could also be complex
fourier = fft(signal)
fourier
N = len(signal)
fourier = empty(N, complex)
for k in range(N):  # equivalent but much slower
    fourier[k] = sum(signal * exp(-1j * 2 * pi * k * arange(N) / N))
timestep = 0.1  # if unit=day -> freq unit=cycles/day
fftfreq(N, d=timestep)  # freqs corresponding to 'fourier'
