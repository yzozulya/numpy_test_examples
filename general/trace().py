from numpy import *

a = arange(12).reshape(3, 4)
a
a.diagonal()
a.trace()
a.diagonal(offset=1)
a.trace(offset=1)
