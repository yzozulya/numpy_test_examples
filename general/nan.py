from numpy import *

sqrt(array([-1.0]))
x = array([2, nan, 1])
isnan(x)  # show which elements are nan
isfinite(x)  # show which elements are not nan/inf/-inf
nansum(x)  # same as sum() but ignore nan elements
nanmax(x)  # same as max() but ignore nan elements
nanmin(x)  # same as min() but ignore nan elements
nanargmin(x)  # same as argmin() but ignore nan elements
nanargmax(x)  # same as argmax() but ignore nan elements
nan_to_num(x)  # replace all nan elements with 0.0
