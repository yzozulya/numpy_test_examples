import numpy as np

x = np.arange(1, 7).reshape(2, 3)
x
x.flat[3]
x.T
x.T.flat[3]
type(x.flat)
x.flat = 3
x
x.flat[[1, 4]] = 1
x
