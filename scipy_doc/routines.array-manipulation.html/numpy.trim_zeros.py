import numpy as np

a = np.array((0, 0, 0, 1, 2, 3, 0, 2, 1, 0))
np.trim_zeros(a)
np.trim_zeros(a, 'b')
np.trim_zeros([0, 1, 2, 0])
