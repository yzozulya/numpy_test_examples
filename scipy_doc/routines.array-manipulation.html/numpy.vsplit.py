import numpy as np

x = np.arange(16.0).reshape(4, 4)
x
np.vsplit(x, 2)
np.vsplit(x, np.array([3, 6]))
x = np.arange(8.0).reshape(2, 2, 2)
x
np.vsplit(x, 2)
