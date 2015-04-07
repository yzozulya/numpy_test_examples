from numpy import *

a = array([5, 15, 25])
a.ptp()  # peak-to-peak = maximum - minimum
a = array([[5, 15, 25], [3, 13, 33]])
a.ptp()
a.ptp(axis=0)  # peak-to-peak value for each of the 3 columns
a.ptp(axis=1)  # peak-to-peak value for each of the 2 rows
