import numpy as np

np.where([[True, False], [True, True]],
         [[1, 2], [3, 4]],
         [[9, 8], [7, 6]])
np.where([[0, 1], [1, 0]])
x = np.arange(9.).reshape(3, 3)
np.where(x > 5)
x[np.where(x > 3.0)]  # Note: result is 1D.
np.where(x < 5, x, -1)  # Note: broadcasting.
goodvalues = [3, 4, 7]
ix = np.in1d(x.ravel(), goodvalues).reshape(x.shape)
ix
np.where(ix)
