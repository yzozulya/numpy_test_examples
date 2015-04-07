import numpy as np
import numpy.ma as ma

dtype = np.dtype({'names': ['foo', 'bar'],
                  'formats': [np.float32, np.int]})

ma.make_mask_descr(dtype)
ma.make_mask_descr(np.float32)
