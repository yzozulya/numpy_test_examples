import numpy as np

a = np.ma.array([1, 2, 3], mask=[False, False, True])
a
a.mean()
