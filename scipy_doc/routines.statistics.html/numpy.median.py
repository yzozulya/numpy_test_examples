import numpy as np

a = np.array([[10, 7, 4], [3, 2, 1]])
a
np.median(a)
np.median(a, axis=0)
np.median(a, axis=1)
m = np.median(a, axis=0)
out = np.zeros_like(m)
np.median(a, axis=0, out=m)
m
b = a.copy()
np.median(b, axis=1, overwrite_input=True)
assert not np.all(a == b)
b = a.copy()
np.median(b, axis=None, overwrite_input=True)
assert not np.all(a == b)
