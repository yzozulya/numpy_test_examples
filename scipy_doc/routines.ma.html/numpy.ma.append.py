import numpy.ma as ma

a = ma.masked_values([1, 2, 3], 2)
b = ma.masked_values([[4, 5, 6], [7, 8, 9]], 7)
print(ma.append(a, b))
