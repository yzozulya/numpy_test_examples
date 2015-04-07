import numpy as np

choices = [[0, 1, 2, 3], [10, 11, 12, 13],
           [20, 21, 22, 23], [30, 31, 32, 33]]
np.choose([2, 3, 1, 0], choices
          # the first element of the result will be the first element of the
          # third (2+1) "array" in choices, namely, 20; the second element
          # will be the second element of the fourth (3+1) choice array, i.e.,
          # 31, etc.
          )
np.choose([2, 4, 1, 0], choices, mode='clip')  # 4 goes to 3 (4-1)
# because there are 4 choice arrays
np.choose([2, 4, 1, 0], choices, mode='wrap')  # 4 goes to (4 mod 4)
# i.e., 0
a = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
choices = [-10, 10]
np.choose(a, choices)
# With thanks to Anne Archibald
a = np.array([0, 1]).reshape((2, 1, 1))
c1 = np.array([1, 2, 3]).reshape((1, 3, 1))
c2 = np.array([-1, -2, -3, -4, -5]).reshape((1, 1, 5))
np.choose(a, (c1, c2))  # result is 2x3x5, res[0,:,:]=c1, res[1,:,:]=c2
