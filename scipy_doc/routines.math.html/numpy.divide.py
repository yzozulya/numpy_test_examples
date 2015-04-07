import numpy as np

np.divide(2.0, 4.0)
x1 = np.arange(9.0).reshape((3, 3))
x2 = np.arange(3.0)
np.divide(x1, x2)
np.divide(2, 4)
np.divide(2, 4.)
np.divide(np.array([0, 1], dtype=int), np.array([0, 0], dtype=int))
old_err_state = np.seterr(divide='raise')
np.divide(1, 0)
ignored_states = np.seterr(**old_err_state)
np.divide(1, 0)
