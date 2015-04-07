import numpy as np

mean = [0, 0]
cov = [[1, 0], [0, 100]]  # diagonal covariance, points lie on x or y-axis
import matplotlib.pyplot as plt

x, y = np.random.multivariate_normal(mean, cov, 5000).T
plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()
mean = (1, 2)
cov = [[1, 0], [1, 0]]
x = np.random.multivariate_normal(mean, cov, (3, 3))
x.shape
print
list((x[0, 0, :] - mean) < 0.6)