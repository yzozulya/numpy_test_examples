from numpy import *

a = array([2, 0, 8, 4, 1])
a.sort()  # in-place sorting with quicksort (default)
a
a.sort(kind='mergesort')  # algorithm options are 'quicksort', 'mergesort' and 'heapsort'
a = array([[8, 4, 1], [2, 0, 9]])
a.sort(axis=0)
a
a = array([[8, 4, 1], [2, 0, 9]])
a.sort(axis=1)  # default axis = -1
a
sort(a)  # there is a functional form
