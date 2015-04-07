import numpy as np

x = np.ma.array([1., -1, np.nan, np.inf], mask=[1] + [0] * 3)
x
np.ma.fix_invalid(x)
fixed = np.ma.fix_invalid(x)
fixed.data
x.data
