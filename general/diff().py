from numpy import *

x = array([0, 1, 3, 9, 5, 10])
diff(x)  # 1st-order differences between the elements of x
diff(x, n=2)  # 2nd-order differences, equivalent to diff(diff(x))
x = array([[1, 3, 6, 10], [0, 5, 6, 8]])
diff(x)  # 1st-order differences between the columns (default: axis=-1)
diff(x, axis=0)  # 1st-order difference between the rows
