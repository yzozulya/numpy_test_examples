from numpy import *

x = arange(5, 0, -1)
print x
criterion = (x <= 2) | (x >= 5)
criterion
indices = where(criterion, 1, 0)
print indices
x[indices]  # integers!
x[criterion]  # bools!
indices = where(criterion)
print indices
x[indices]
