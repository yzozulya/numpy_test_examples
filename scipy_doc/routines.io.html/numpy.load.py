import numpy as np

np.save('/tmp/123', np.array([[1, 2, 3], [4, 5, 6]]))
np.load('/tmp/123.npy')
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2])
np.savez('/tmp/123.npz', a=a, b=b)
data = np.load('/tmp/123.npz')
data['a']
data['b']
data.close()
X = np.load('/tmp/123.npy', mmap_mode='r')
X[1, :]
