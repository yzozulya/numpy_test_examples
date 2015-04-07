import numpy as np

a = np.ma.array([3, 2, 1], mask=[False, False, True])
a
a.argsort()
