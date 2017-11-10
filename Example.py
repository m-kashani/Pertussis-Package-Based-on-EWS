# An example of using ews_plot.

import numpy as np
import ews
import ews_plot

#Replace with correct data:
x = np.random.random(300)

ews_df = ews.get_ews(x, windowsize=100, ac_lag=1)

# Replace this with correct time from data:
ews_df["Time"] = np.arange(len(x))
signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

ews_plot.ews_plot (ews_df,signals,filename="./test.pdf")