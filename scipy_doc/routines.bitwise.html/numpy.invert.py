import numpy as np
from numpy import uint8, uint16, int8, array

x = 1
np.bitwise_not is np.invert
np.invert(np.array([13], dtype=uint8))
np.binary_repr(x, width=8)
np.binary_repr(242, width=8)
np.invert(np.array([13], dtype=uint16))
np.binary_repr(x, width=16)
np.binary_repr(65522, width=16)
np.invert(np.array([13], dtype=int8))
np.binary_repr(-14, width=8)
np.invert(array([True, False]))
