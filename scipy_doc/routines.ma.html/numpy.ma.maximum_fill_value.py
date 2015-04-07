import numpy as np
import numpy.ma as ma

a = np.int8()
np.ma.maximum_fill_value(a)
a = np.int32()
ma.maximum_fill_value(a)
a = np.array([1, 2, 3], dtype=np.int8)
ma.maximum_fill_value(a)
a = np.array([1, 2, 3], dtype=np.float32)
ma.maximum_fill_value(a)
