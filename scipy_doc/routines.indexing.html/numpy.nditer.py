import numpy as np


def outer_it(x, y, out=None):
    mulop = np.multiply

    it = np.nditer([x, y, out], ['external_loop'],
                   [['readonly'], ['readonly'], ['writeonly', 'allocate']],
                   op_axes=[range(x.ndim) + [-1] * y.ndim,
                            [-1] * x.ndim + range(y.ndim),
                            None])

    for (a_, b_, c) in it:
        mulop(a_, b_, out=c)

    return it.operands[2]


def luf(lamdaexpr, *args, **kwargs):
    """luf(lambdaexpr, op1, ..., opn, out=None, order='K', casting='safe', buffersize=0)"""
    nargs = len(args)
    op = (kwargs.get('out', None),) + args
    it = np.nditer(op, ['buffered', 'external_loop'],
                   [['writeonly', 'allocate', 'no_broadcast']] +
                   [['readonly', 'nbo', 'aligned']] * nargs,
                   order=kwargs.get('order', 'K'),
                   casting=kwargs.get('casting', 'safe'),
                   buffersize=kwargs.get('buffersize', 0))
    while not it.finished:
        it[0] = lamdaexpr(*it[1:])
        it.iternext()
    return it.operands[0]


a = np.arange(2) + 1
b = np.arange(3) + 1
outer_it(a, b)
a = np.arange(5)
b = np.ones(5)
luf(lambda i, j: i * i + j / 2, a, b)
