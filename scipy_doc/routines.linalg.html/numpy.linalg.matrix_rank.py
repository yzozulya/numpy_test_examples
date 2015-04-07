import numpy as np
from numpy.linalg import matrix_rank

matrix_rank(np.eye(4))  # Full rank matrix
I = np.eye(4)
I[-1, -1] = 0.  # rank deficient matrix
matrix_rank(I)
matrix_rank(np.ones((4,)))  # 1 dimension - rank 1 unless all 0
matrix_rank(np.zeros((4,)))
