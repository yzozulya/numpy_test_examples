import numpy as np

x = np.ma.array(np.arange(9).reshape(3, 3), mask=[[1, 0, 0],
                                                  [1, 0, 0],
                                                  [0, 0, 0]])
x
np.ma.extras.compress_rowcols(x)
np.ma.extras.compress_rowcols(x, 0)
np.ma.extras.compress_rowcols(x, 1)
