import numpy as np

np.array([1, 2, 3])
np.array([1, 2, 3.0])
np.array([[1, 2], [3, 4]])
np.array([1, 2, 3], ndmin=2)
np.array([1, 2, 3], dtype=complex)
x = np.array([(1, 2), (3, 4)], dtype=[('a', '<i4'), ('b', '<i4')])
x['a']
np.array(np.mat('1 2; 3 4'))
np.array(np.mat('1 2; 3 4'), subok=True)
