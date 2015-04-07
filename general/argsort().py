from numpy import *

a = array([2, 0, 8, 4, 1])
ind = a.argsort()  # indices of sorted array using quicksort (default)
ind
a[ind]  # same effect as a.sort()
ind = a.argsort(kind='merge')  # algorithm options are 'quicksort', 'mergesort' and 'heapsort'
a = array([[8, 4, 1], [2, 0, 9]])
ind = a.argsort(axis=0)  # sorts on columns. NOT the same as a.sort(axis=1)
ind
a[ind, [[0, 1, 2], [0, 1, 2]]]  # 2-D arrays need fancy indexing if you want to sort them.
ind = a.argsort(axis=1)  # sort along rows. Can use a.argsort(axis=-1) for last axis.
ind
a = ones(17)
a.argsort()  # quicksort doesn't preserve original order.
a.argsort(kind="mergesort")  # mergesort preserves order when possible. It is a stable sort.
ind = argsort(a)  # there is a functional form
