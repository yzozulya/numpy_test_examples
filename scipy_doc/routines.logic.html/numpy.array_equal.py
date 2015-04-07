import numpy as np

np.array_equal([1, 2], [1, 2])
np.array_equal(np.array([1, 2]), np.array([1, 2]))
np.array_equal([1, 2], [1, 2, 3])
np.array_equal([1, 2], [1, 4])
