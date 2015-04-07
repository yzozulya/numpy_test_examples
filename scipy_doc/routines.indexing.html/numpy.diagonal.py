import numpy as np

a = np.arange(4).reshape(2, 2)
a
a.diagonal()
a.diagonal(1)
a = np.arange(8).reshape(2, 2, 2)
a
a.diagonal(0,  # Main diagonals of two arrays created by skipping
           0,  # across the outer(left)-most axis last and
           1)  # the "middle" (row) axis first.
a[:, :, 0]  # main diagonal is [0 6]
a[:, :, 1]  # main diagonal is [1 7]
