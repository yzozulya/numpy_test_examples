import numpy as np

np.ma.array([1, 2, 3]).all()
a = np.ma.array([1, 2, 3], mask=True)
(a.all() is np.ma.masked)
