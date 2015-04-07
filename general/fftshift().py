from numpy import *
from numpy.fft import *

signal = array([-2., 8., -6., 4., 1., 0., 3., 5.])
fourier = fft(signal)
N = len(signal)
timestep = 0.1  # if unit=day -> freq unit=cycles/day
freq = fftfreq(N, d=timestep)  # freqs corresponding to 'fourier'
freq
freq = fftshift(freq)  # freqs in ascending order
freq
fourier = fftshift(fourier)  # adjust fourier to new freq order
freq = ifftshift(freq)  # undo previous frequency shift
fourier = ifftshift(fourier)  # undo previous fourier shift
