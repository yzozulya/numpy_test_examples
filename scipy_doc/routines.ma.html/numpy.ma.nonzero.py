import numpy as np
import numpy.ma as ma

x = ma.array(np.eye(3))
x
x.nonzero()
x[1, 1] = ma.masked
x
x.nonzero()
np.transpose(x.nonzero())
a = ma.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a > 3
ma.nonzero(a > 3)
(a > 3).nonzero()
