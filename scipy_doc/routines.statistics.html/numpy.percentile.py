import numpy as np

a = np.array([[10, 7, 4], [3, 2, 1]])
a
np.percentile(a, 50)
np.percentile(a, 50, axis=0)
np.percentile(a, 50, axis=1)
m = np.percentile(a, 50, axis=0)
out = np.zeros_like(m)
np.percentile(a, 50, axis=0, out=m)
m
b = a.copy()
np.percentile(b, 50, axis=1, overwrite_input=True)
assert not np.all(a == b)
b = a.copy()
np.percentile(b, 50, axis=None, overwrite_input=True)
