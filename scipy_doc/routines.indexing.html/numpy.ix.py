import numpy as np

a = np.arange(10).reshape(2, 5)
a
ixgrid = np.ix_([0, 1], [2, 4])
ixgrid
ixgrid[0].shape, ixgrid[1].shape
a[ixgrid]
