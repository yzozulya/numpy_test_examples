import numpy as np

r = np.core.records.fromrecords([(456, 'dbe', 1.2), (2, 'de', 1.3)],
                                names='col1,col2,col3')
print
r[0]
r.col1
r.col2
import pickle

print
pickle.loads(pickle.dumps(r))
