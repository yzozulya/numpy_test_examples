import numpy as np
from numpy import ma

a = ma.array([[1, 2, 3], [4, 5, 6]], mask=[[1, 0, 0], [0, 0, 0]])
b = ma.array([[1, 2], [3, 4], [5, 6]], mask=[[1, 0], [0, 0], [0, 0]])
np.ma.dot(a, b)
np.ma.dot(a, b, strict=True)
