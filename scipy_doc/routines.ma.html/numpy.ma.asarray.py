import numpy as np

x = np.arange(10.).reshape(2, 5)
x
np.ma.asarray(x)
type(np.ma.asarray(x))
