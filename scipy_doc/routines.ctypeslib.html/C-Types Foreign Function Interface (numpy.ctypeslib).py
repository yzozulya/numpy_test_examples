import numpy as np


def somefunc(*args, **kwargs):
    print(args, kwargs)


somefunc.argtypes = [np.ctypeslib.ndpointer(dtype=np.float64,
                                            ndim=1,
                                            flags='C_CONTIGUOUS')]

somefunc(np.array([1, 2, 3], dtype=np.float64))