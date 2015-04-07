import numpy as np

np.ldexp(5, np.arange(4))
x = np.arange(6)
np.ldexp(*np.frexp(x))
