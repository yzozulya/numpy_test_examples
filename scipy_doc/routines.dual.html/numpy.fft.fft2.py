import numpy as np

a = np.mgrid[:5, :5][0]
np.fft.fft2(a)
