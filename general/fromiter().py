from numpy import *
import itertools

mydata = [[55.5, 40], [60.5, 70]]  # List of lists
mydescriptor = {'names': ('weight', 'age'), 'formats': (float32, int32)}  # Descriptor of the data
myiterator = itertools.imap(tuple, mydata)  # Clever way of putting list of lists into iterator
a = fromiter(myiterator, dtype=mydescriptor)
a
