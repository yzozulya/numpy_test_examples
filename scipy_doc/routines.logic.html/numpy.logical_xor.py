import numpy as np

np.logical_xor(True, False)
np.logical_xor([True, True, False, False], [True, False, True, False])
x = np.arange(5)
np.logical_xor(x < 1, x > 3)
np.logical_xor(0, np.eye(2))
