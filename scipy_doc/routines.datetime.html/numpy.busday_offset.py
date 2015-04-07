import numpy as np
# First business day in October 2011 (not accounting for holidays)
np.busday_offset('2011-10', 0, roll='forward')
# Last business day in February 2012 (not accounting for holidays)
np.busday_offset('2012-03', -1, roll='forward')
# Third Wednesday in January 2011
np.busday_offset('2011-01', 2, roll='forward', weekmask='Wed')
# 2012 Mother's Day in Canada and the U.S.
np.busday_offset('2012-05', 1, roll='forward', weekmask='Sun')
# First business day on or after a date
np.busday_offset('2011-03-20', 0, roll='forward')
np.busday_offset('2011-03-22', 0, roll='forward')
# First business day after a date
np.busday_offset('2011-03-20', 1, roll='backward')
np.busday_offset('2011-03-22', 1, roll='backward')
