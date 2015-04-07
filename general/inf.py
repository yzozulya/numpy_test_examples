from numpy import *

exp(array([1000.]))  # inf = infinite = number too large to represent, machine dependent
x = array([2, -inf, 1, inf])
isfinite(x)  # show which elements are not nan/inf/-inf
isinf(x)  # show which elements are inf/-inf
isposinf(x)  # show which elements are inf
isneginf(x)  # show which elements are -inf
nan_to_num(x)  # replace -inf/inf with most negative/positive representable number
