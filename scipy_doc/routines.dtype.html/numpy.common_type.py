import numpy as np

np.common_type(np.arange(2, dtype=np.float32))
np.common_type(np.arange(2, dtype=np.float32), np.arange(2))
np.common_type(np.arange(4), np.array([45, 6.j]), np.array([45.0]))
