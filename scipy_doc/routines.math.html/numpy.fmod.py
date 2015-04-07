import numpy as np

np.fmod([-3, -2, -1, 1, 2, 3], 2)
np.remainder([-3, -2, -1, 1, 2, 3], 2)
np.fmod([5, 3], [2, 2.])
a = np.arange(-3, 3).reshape(3, 2)
a
np.fmod(a, [2, 2])
