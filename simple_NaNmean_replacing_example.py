#Simple example of using np.nanmean to fill nan numbers in our numpy array.
import numpy as np

a = np.array([1, np.nan , 3,4])

a[np.isnan(a)] = np.nanmean(a)

print(a)