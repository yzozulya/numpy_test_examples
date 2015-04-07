import numpy as np

x = [1, 2, 3]
y = [4, 5, 6]
np.cross(x, y)
x = [1, 2]
y = [4, 5, 6]
np.cross(x, y)
x = [1, 2, 0]
y = [4, 5, 6]
np.cross(x, y)
x = [1, 2]
y = [4, 5]
np.cross(x, y)
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[4, 5, 6], [1, 2, 3]])
np.cross(x, y)
np.cross(x, y, axisc=0)
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array([[7, 8, 9], [4, 5, 6], [1, 2, 3]])
np.cross(x, y)
np.cross(x, y, axisa=0, axisb=0)
