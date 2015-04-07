from matplotlib.mlab import ma
import numpy as np

x = ma.array([1, 2, 3], mask=[0, 1, 0])
x[1] is ma.masked
x[-1] = ma.masked
x
x = ma.array(np.matrix([[1, 2], [3, 4]]), mask=[[0, 1], [1, 0]])
x.data
x = ma.array([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)],
             mask=[(0, 0), (1, 0), (1, 1), (0, 1), (0, 0)],
             dtype=[('a', int), ('b', int)])
x.recordmask
x = ma.array(np.matrix([[1, 2], [3, 4]]), mask=[[0, 0], [1, 0]])
x.baseclass
