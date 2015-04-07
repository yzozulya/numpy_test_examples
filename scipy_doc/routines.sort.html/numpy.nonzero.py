import numpy as np

x = np.eye(3)
x
np.nonzero(x)
x[np.nonzero(x)]
np.transpose(np.nonzero(x))
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a > 3
np.nonzero(a > 3)
(a > 3).nonzero()
