import numpy as np

x = np.array([[0, 2], [1, 1], [2, 0]]).T
x
np.cov(x)
x = [-2.1, -1, 4.3]
y = [3, 1.1, 0.12]
X = np.vstack((x, y))
print
np.cov(X)
print
np.cov(x, y)
print
np.cov(x)
