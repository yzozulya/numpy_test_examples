import numpy as np

x = np.array([[1, 2, 3]])
y = np.array([[1], [2], [3]])
np.broadcast_arrays(x, y)
[np.array(a) for a in np.broadcast_arrays(x, y)]
