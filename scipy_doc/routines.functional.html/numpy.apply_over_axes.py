import numpy as np

a = np.arange(24).reshape(2, 3, 4)
a
np.apply_over_axes(np.sum, a, [0, 2])
np.sum(a, axis=(0, 2), keepdims=True)
