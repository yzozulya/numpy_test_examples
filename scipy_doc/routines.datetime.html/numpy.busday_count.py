import numpy as np
# Number of weekdays in January 2011
np.busday_count('2011-01', '2011-02')
# Number of weekdays in 2011
np.busday_count('2011', '2012')  # Number of Saturdays in 2011
np.busday_count('2011', '2012', weekmask='Sat')
