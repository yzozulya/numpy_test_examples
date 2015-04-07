import numpy as np

m1 = np.ma.make_mask([0, 1, 1, 0])
m2 = np.ma.make_mask([1, 0, 0, 0])
np.ma.mask_or(m1, m2)
