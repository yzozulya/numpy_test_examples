import numpy as np

x = np.arange(9).reshape((3, 3))
x
np.diag(x)
np.diag(x, k=1)
np.diag(x, k=-1)
np.diag(np.diag(x))
