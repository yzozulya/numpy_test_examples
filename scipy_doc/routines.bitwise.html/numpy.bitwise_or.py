import numpy as np

np.bitwise_or(13, 16)
np.binary_repr(29)
np.bitwise_or(32, 2)
np.bitwise_or([33, 4], 1)
np.bitwise_or([33, 4], [1, 2])
np.bitwise_or(np.array([2, 5, 255]), np.array([4, 4, 4]))
np.array([2, 5, 255]) | np.array([4, 4, 4])
np.bitwise_or(np.array([2, 5, 255, 2147483647L], dtype=np.int32),
              np.array([4, 4, 4, 2147483647L], dtype=np.int32))
np.bitwise_or([True, True], [False, True])
