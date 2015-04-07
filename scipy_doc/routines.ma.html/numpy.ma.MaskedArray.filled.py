import numpy as np

x = np.ma.array([1, 2, 3, 4, 5], mask=[0, 0, 1, 0, 1], fill_value=-999)
x.filled()
type(x.filled())
x = np.ma.array(np.matrix([[1, 2], [3, 4]]), mask=[[0, 1], [1, 0]])
x.filled()
