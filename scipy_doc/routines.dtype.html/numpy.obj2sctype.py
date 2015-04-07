import numpy as np

np.obj2sctype(np.int32)
np.obj2sctype(np.array([1., 2.]))
np.obj2sctype(np.array([1.j]))
np.obj2sctype(dict)
np.obj2sctype('string')
np.obj2sctype(1, default=list)
