import numpy as np

np.unravel_index([22, 41, 37], (7, 6))
np.unravel_index([31, 41, 13], (7, 6), order='F')
np.unravel_index(1621, (6, 7, 8, 9))
