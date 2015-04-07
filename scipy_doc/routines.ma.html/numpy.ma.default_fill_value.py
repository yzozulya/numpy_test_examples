import numpy as np

np.ma.default_fill_value(1)
np.ma.default_fill_value(np.array([1.1, 2., np.pi]))
np.ma.default_fill_value(np.dtype(complex))
