import numpy as np

a = ma.array([1e10, 1e-7, 42.0], mask=[0, 0, 1])
a
b = array([1e10, 1e-7, -42.0])
b
ma.allequal(a, b, fill_value=False)
ma.allequal(a, b)
