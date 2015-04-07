import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
a
np.compress([0, 1], a, axis=0)
np.compress([False, True, True], a, axis=0)
np.compress([False, True], a, axis=1)
np.compress([False, True], a)
