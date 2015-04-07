import numpy as np
import numpy.ma as ma

ma.make_mask_none((3,))
dtype = np.dtype({'names': ['foo', 'bar'],
                  'formats': [np.float32, np.int]})

ma.make_mask_none((3,), dtype=dtype)
