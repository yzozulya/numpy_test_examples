import numpy as np
# Some important days in July
bdd = np.busdaycalendar(
    holidays=['2011-07-01', '2011-07-04', '2011-07-17'])
# Default is Monday to Friday weekdays
bdd.weekmask
# Any holidays already on the weekend are removed
bdd.holidays
