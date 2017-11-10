# An example of using ews_plot.

import numpy as np
import ews
import ews_plot


x = np.array([11,29,3,4,5,6,np.nan,8,9,10,11,np.nan,12,4,15,6,45,30,36,33,np.nan,20,np.nan]) # np.array(List)
x[np.isnan(x)] = np.nanmean(x)

ews_df = ews.get_ews(x, windowsize=5, ac_lag=1)

ews_df["Time"] = np.arange(len(x))
signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

ews_plot.ews_plot (ews_df,signals,filename="./Test_MeanNan_Using.pdf")

#----------------

#x = np.array([11,29,3,4,5,6,np.nan,8,9,10,11,np.nan,12,4,15,6,45,30,36,33,np.nan,20,np.nan])
#a = np.nanmean(x)

'''
ews_df = ews.get_ews(x, windowsize=5, ac_lag=1)

ews_df["Time"] = np.arange(len(x))
signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

ews_plot.ews_plot (ews_df,signals,filename="./MeanNan_Using_test.pdf")
'''
