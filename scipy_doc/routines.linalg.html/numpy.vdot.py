import numpy as np

a = np.array([1 + 2j, 3 + 4j])
b = np.array([5 + 6j, 7 + 8j])
np.vdot(a, b)
np.vdot(b, a)
a = np.array([[1, 4], [5, 6]])
b = np.array([[4, 1], [2, 2]])
np.vdot(a, b)
np.vdot(b, a)
1 * 4 + 4 * 1 + 5 * 2 + 6 * 2
