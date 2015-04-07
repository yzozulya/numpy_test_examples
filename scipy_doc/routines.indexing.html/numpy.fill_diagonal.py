import numpy as np

a = np.zeros((3, 3), int)
np.fill_diagonal(a, 5)
a
a = np.zeros((3, 3, 3, 3), int)
np.fill_diagonal(a, 4)
a[0, 0]
a[1, 1]
a[2, 2]
