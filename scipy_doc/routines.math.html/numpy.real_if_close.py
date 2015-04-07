import numpy as np

np.finfo(np.float).eps
np.real_if_close([2.1 + 4e-14j], tol=1000)
np.real_if_close([2.1 + 4e-13j], tol=1000)
