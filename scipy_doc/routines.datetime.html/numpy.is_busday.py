import numpy as np
# The weekdays are Friday, Saturday, and Monday
np.is_busday(['2011-07-01', '2011-07-02', '2011-07-18'],
             holidays=['2011-07-01', '2011-07-04', '2011-07-17'])
