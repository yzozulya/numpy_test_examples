import numpy as np

np.r_[np.array([1, 2, 3]), 0, 0, np.array([4, 5, 6])]
np.r_[-1:1:6j, [0] * 3, 5, 6]
a = np.array([[0, 1, 2], [3, 4, 5]])
np.r_['-1', a, a]  # concatenate along last axis
np.r_['0,2', [1, 2, 3], [4, 5, 6]]  # concatenate along first axis, dim>=2
np.r_['0,2,0', [1, 2, 3], [4, 5, 6]]
np.r_['1,2,0', [1, 2, 3], [4, 5, 6]]
np.r_['r', [1, 2, 3], [4, 5, 6]]
