import numpy as np

a = np.arange(9).reshape((3, 3))
mask = np.zeros_like(a)
mask[1:, 1:] = 1
ma = np.ma.array(a, mask=mask)
np.array(ma[~ma.mask])
np.ma.extras.notmasked_contiguous(ma)
