import numpy as np

np.zeros(5)
np.zeros((5,), dtype=np.int)
np.zeros((2, 1))
s = (2, 2)
np.zeros(s)
np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')])  # custom dtype
