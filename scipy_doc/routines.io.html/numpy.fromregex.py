import numpy as np

f = open('test.dat', 'w')
f.write("1312 foo\n1534  bar\n444   qux")
f.close()
regexp = r"(\d+)\s+(...)"  # match [digits, whitespace, anything]
output = np.fromregex('test.dat', regexp,
                      [('num', np.int64), ('key', 'S3')])
output
output['num']
