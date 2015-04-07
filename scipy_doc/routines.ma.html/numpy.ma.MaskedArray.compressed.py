import numpy as np

x = np.ma.array(np.arange(5), mask=[0] * 2 + [1] * 3)
x.compressed()
type(x.compressed())
