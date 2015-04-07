import numpy as np

x = np.array([1, 2, 4, 7, 0])
np.ediff1d(x)
np.ediff1d(x, to_begin=-99, to_end=np.array([88, 99]))
y = [[1, 2, 4], [1, 6, 24]]
np.ediff1d(y)
