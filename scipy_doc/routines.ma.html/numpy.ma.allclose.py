from matplotlib.mlab import ma

a = ma.array([1e10, 1e-7, 42.0], mask=[0, 0, 1])
a
b = ma.array([1e10, 1e-8, -42.0], mask=[0, 0, 1])
ma.allclose(a, b)
a = ma.array([1e10, 1e-8, 42.0], mask=[0, 0, 1])
b = ma.array([1.00001e10, 1e-9, -42.0], mask=[0, 0, 1])
ma.allclose(a, b)
ma.allclose(a, b, masked_equal=False)
a = ma.array([1e10, 1e-8, 42.0], mask=[0, 0, 1])
b = ma.array([1.00001e10, 1e-9, 42.0], mask=[0, 0, 1])
ma.allclose(a, b)
ma.allclose(a, b, masked_equal=False)
