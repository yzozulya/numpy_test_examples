import numpy as np

a = np.array([[1, 4], [3, 1]])
np.sort(a)  # sort along the last axis
np.sort(a, axis=None)  # sort the flattened array
np.sort(a, axis=0)  # sort along the first axis
dtype = [('name', 'S10'), ('height', float), ('age', int)]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38),
          ('Galahad', 1.7, 38)]
a = np.array(values, dtype=dtype)  # create a structured array
np.sort(a, order='height')
np.sort(a, order=['age', 'height'])               
