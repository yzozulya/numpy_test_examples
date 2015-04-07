import numpy as np

x = np.array([3, 1, 2])
np.argsort(x)
x = np.array([[0, 3], [2, 2]])
x
np.argsort(x, axis=0)
np.argsort(x, axis=1)
x = np.array([(1, 0), (0, 1)], dtype=[('x', '<i4'), ('y', '<i4')])
x
np.argsort(x, order=('x', 'y'))
np.argsort(x, order=('y', 'x'))
