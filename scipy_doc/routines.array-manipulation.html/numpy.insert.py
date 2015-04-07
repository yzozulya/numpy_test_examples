import numpy as np

a = np.array([[1, 1], [2, 2], [3, 3]])
a
np.insert(a, 1, 5)
np.insert(a, 1, 5, axis=1)
np.array_equal(np.insert(a, 1, [1, 2, 3], axis=1),
               np.insert(a, [1], [[1], [2], [3]], axis=1))
b = a.flatten()
b
np.insert(b, [2, 2], [5, 6])
np.insert(b, slice(2, 4), [5, 6])
np.insert(b, [2, 2], [7.13, False])  # type casting
x = np.arange(8).reshape(2, 4)
idx = (1, 3)
np.insert(x, idx, 999, axis=1)
