import numpy as np

x = np.ma.array(np.arange(8), mask=[0] * 4 + [1] * 4)
np.ma.extras.median(x)
x = np.ma.array(np.arange(10).reshape(2, 5), mask=[0] * 6 + [1] * 4)
np.ma.extras.median(x)
np.ma.extras.median(x, axis=-1, overwrite_input=True)
