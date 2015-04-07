import numpy as np

x = np.arange(6).reshape(2, 3)
np.ascontiguousarray(x, dtype=np.float32)
x.flags['C_CONTIGUOUS']
