import numpy as np
import numpy.ma as ma

ma.masked_all((3, 3))
a = ma.masked_all((3, 3))
a.dtype
a = ma.masked_all((3, 3), dtype=np.int32)
a.dtype
