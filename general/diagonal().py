from numpy import *

a = arange(12).reshape(3, 4)
print a
a.diagonal()
a.diagonal(offset=1)
diagonal(a)  # Also this form exists
