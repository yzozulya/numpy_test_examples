import numpy as np

a = np.ones((2, 2, 2))
np.fft.rfftn(a)
np.fft.rfftn(a, axes=(2, 0))
