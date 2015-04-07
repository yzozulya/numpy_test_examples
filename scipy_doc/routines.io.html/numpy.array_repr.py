import numpy as np

np.array_repr(np.array([1, 2]))
np.array_repr(np.ma.array([0.]))
np.array_repr(np.array([], np.int32))
x = np.array([1e-6, 4e-7, 2, 3])
np.array_repr(x, precision=6, suppress_small=True)
