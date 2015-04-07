import numpy as np

np.mintypecode(['d', 'f', 'S'])
x = np.array([1.1, 2 - 3.j])
np.mintypecode(x)
np.mintypecode('abceh', default='G')
