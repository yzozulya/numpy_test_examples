import numpy as np

surnames = ('Hertz', 'Galilei', 'Hertz')
first_names = ('Heinrich', 'Galileo', 'Gustav')
ind = np.lexsort((first_names, surnames))
ind
[surnames[i] + ", " + first_names[i] for i in ind]
a = [1, 5, 1, 4, 3, 4, 4]  # First column
b = [9, 4, 0, 4, 0, 2, 1]  # Second column
ind = np.lexsort((b, a))  # Sort by a, then by b
print
ind
[(a[i], b[i]) for i in ind]
[(a[i], b[i]) for i in np.argsort(a)]
x = np.array([(1, 9), (5, 4), (1, 0), (4, 4), (3, 0), (4, 2), (4, 1)],
             dtype=np.dtype([('x', int), ('y', int)]))
np.argsort(x)  # or np.argsort(x, order=('x', 'y'))
