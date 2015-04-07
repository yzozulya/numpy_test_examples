import numpy as np

charar = np.chararray((3, 3))
charar[:] = 'a'
charar
charar = np.chararray(charar.shape, itemsize=5)
charar[:] = 'abc'
charar
