from numpy import *

a = array([10, 20, 30, 40])
insert(a, [1, 3], 50)  # insert value 50 before elements [1] and [3]
insert(a, [1, 3], [50, 60])  # insert value 50 before element [1] and value 60 before element [3]
a = array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
insert(a, [1, 2], 100, axis=0)  # insert row with values 100 before row[1] and before row[2]
insert(a, [0, 1], [[100], [200]], axis=0)
insert(a, [0, 1], [100, 200], axis=1)
