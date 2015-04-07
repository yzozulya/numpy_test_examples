import numpy as np

x = np.ma.array(np.arange(9.).reshape(3, 3), mask=[[0, 1, 0],
                                                   [1, 0, 1],
                                                   [0, 1, 0]])
print
x
np.ma.where(x > 5)  # return the indices where x > 5
print
np.ma.where(x > 5, x, -3.1416)
