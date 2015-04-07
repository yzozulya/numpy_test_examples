import numpy as np

oct_array = np.frompyfunc(oct, 1, 1)
oct_array(np.array((10, 30, 100)))
np.array((oct(10), oct(30), oct(100)))  # for comparison
