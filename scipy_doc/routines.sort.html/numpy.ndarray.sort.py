import numpy as np

a = np.array([[1, 4], [3, 1]])
a.sort(axis=1)
a
a.sort(axis=0)
a
a = np.array([('a', 2), ('c', 1)], dtype=[('x', 'S1'), ('y', int)])
print(a.sort(order='y'))
print(a)
