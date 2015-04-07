import numpy as np

np.set_printoptions(precision=4)
print
np.array([1.123456789])
np.set_printoptions(threshold=5)
print
np.arange(10)
eps = np.finfo(float).eps
x = np.arange(4.)
x ** 2 - (x + eps) ** 2
np.set_printoptions(suppress=True)
x ** 2 - (x + eps) ** 2
np.set_printoptions(formatter={'all': lambda x_: 'int: ' + str(-x_)})
x = np.arange(3)
x
np.set_printoptions()  # formatter gets reset
x
np.set_printoptions(edgeitems=3, infstr='inf',
                    linewidth=75, nanstr='nan', precision=8,
                    suppress=False, threshold=1000, formatter=None)
