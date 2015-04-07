import numpy as np
import numpy.ma as ma

m = ma.masked_equal([0, 1, 0, 2, 3], 0)
m
ma.is_mask(m)
ma.is_mask(m.mask)
m = [False, True, False]
ma.is_mask(m)
m = np.array([False, True, False])
m
ma.is_mask(m)
dtype = np.dtype({'names': ['monty', 'pithon'], })
dtype
m = np.array([(True, False), (False, True), (True, False)], )
m
ma.is_mask(m)
