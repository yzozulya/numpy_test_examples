import numpy as np


def myfunc(a, b):
    """Return a-b if a>b, otherwise return a+b"""
    if a > b:
        return a - b
    else:
        return a + b


vfunc = np.vectorize(myfunc)
vfunc([1, 2, 3, 4], 2)
vfunc.__doc__
vfunc = np.vectorize(myfunc, doc='Vectorized `myfunc`')
vfunc.__doc__
out = vfunc([1, 2, 3, 4], 2)
type(out[0])
vfunc = np.vectorize(myfunc, otypes=[np.float])
out = vfunc([1, 2, 3, 4], 2)
type(out[0])


def mypolyval(p, x):
    _p = list(p)
    res = _p.pop(0)
    while _p:
        res = res * x + _p.pop(0)
    return res


vpolyval = np.vectorize(mypolyval, excluded=['p'])
vpolyval(p=[1, 2, 3], x=[0, 1])
vpolyval.excluded.add(0)
vpolyval([1, 2, 3], x=[0, 1])
