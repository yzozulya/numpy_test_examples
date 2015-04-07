import numpy as np

x = np.array([[[0], [1], [2]]])
x.shape
np.squeeze(x).shape
np.squeeze(x, axis=(2,)).shape
