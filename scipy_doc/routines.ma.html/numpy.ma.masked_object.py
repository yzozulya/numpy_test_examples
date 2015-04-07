import numpy as np
import numpy.ma as ma

food = np.array(['green_eggs', 'ham'], dtype=object)
# don't eat spoiled food
eat = ma.masked_object(food, 'green_eggs')
print
eat
# plain ol` ham is boring
fresh_food = np.array(['cheese', 'ham', 'pineapple'], dtype=object)
eat = ma.masked_object(fresh_food, 'green_eggs')
print
eat
eat
