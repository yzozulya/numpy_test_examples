import numpy as np

np.dot(3, 4)
np.dot([2j, 3j], [2j, 3j])
a = [[1, 0], [0, 1]]
b = [[4, 1], [2, 2]]
np.dot(a, b)
a = np.arange(3 * 4 * 5 * 6).reshape((3, 4, 5, 6))
b = np.arange(3 * 4 * 5 * 6)[::-1].reshape((5, 4, 6, 3))
np.dot(a, b)[2, 3, 2, 1, 2, 2]
sum(a[2, 3, 2, :] * b[1, 2, :, 2])
