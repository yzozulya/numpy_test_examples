import numpy as np
from numpy import linalg as la

a = np.array([[1, -2j], [2j, 5]])
la.eigvalsh(a)
