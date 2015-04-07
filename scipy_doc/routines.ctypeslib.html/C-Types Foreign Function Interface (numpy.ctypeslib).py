import numpy as np

clib.somefunc.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64,
                                                 ndim=1,
                                                 flags='C_CONTIGUOUS')]

clib.somefunc(np.array([1, 2, 3], dtype=np.float64))

