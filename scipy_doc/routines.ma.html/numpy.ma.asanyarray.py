import numpy as np

x = np.arange(10.).reshape(2, 5)
x
np.ma.asanyarray(x)
type(np.ma.asanyarray(x))
