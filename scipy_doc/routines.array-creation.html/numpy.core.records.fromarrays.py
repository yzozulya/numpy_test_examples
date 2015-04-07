import numpy as np

x1 = np.array([1, 2, 3, 4])
x2 = np.array(['a', 'dd', 'xyz', '12'])
x3 = np.array([1.1, 2, 3, 4])
r = np.core.records.fromarrays([x1, x2, x3], names='a,b,c')
print
r[1]
x1[1] = 34
r.a
