import numpy as np


def my_func(a):
    """Average first and last element of a 1-D array"""
    return (a[0] + a[-1]) * 0.5


b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.apply_along_axis(my_func, 0, b)
np.apply_along_axis(my_func, 1, b)
b = np.array([[8, 1, 7], [4, 3, 9], [5, 2, 6]])
np.apply_along_axis(sorted, 1, b)
