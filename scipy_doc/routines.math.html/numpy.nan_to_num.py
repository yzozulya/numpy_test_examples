import numpy as np

np.set_printoptions(precision=8)
x = np.array([np.inf, -np.inf, np.nan, -128, 128])
np.nan_to_num(x)
