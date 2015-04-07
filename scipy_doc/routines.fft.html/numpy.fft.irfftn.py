import numpy as np

a = np.zeros((3, 2, 2))
a[0, 0, 0] = 3 * 2 * 2
np.fft.irfftn(a)
