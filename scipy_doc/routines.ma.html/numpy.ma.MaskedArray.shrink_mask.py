import numpy as np

x = np.ma.array([[1, 2], [3, 4]], mask=[0] * 4)
x.mask
x.shrink_mask()
x.mask
