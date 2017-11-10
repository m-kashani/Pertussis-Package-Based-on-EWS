# Running EWS on California data (All trend-seasonal-log(observed))
# NaNs are filled by meaning/mode imputation.

import matplotlib.pyplot as plt ;
import numpy as np ;
import pandas as pd ;
import statsmodels.api as sm

plt.close("all")

#================================== Reading the data and Making Time Series ============================================

# Getting the data.

data_df = pd.read_csv('pertussis.51.12.csv')

# Making the time Series.
Dates = data_df [ ["YEAR","MONTH"] ]
time = Dates['YEAR'].astype(str) + "-" + Dates['MONTH'].astype(str) + "-01" #For each state ?
time = pd.to_datetime(time , format = '%Y-%m-%d')

#====================================== Solving time problem [ns ] to float[64] =======================================

# Making the time_series based on float[64]

Y = data_df["YEAR"]
M = data_df["MONTH"]
New_M = M / 12.0   # one way
Time_Series = Y.values + New_M.values

#=============================================== State name ============================================================

# Get The name of the state to use in the future.

state_name = "California"

#================================================  Make stl  ===========================================================

# Get The name of the state and doing the moving average.

state = ( data_df[state_name] )

state.index = pd.DatetimeIndex(time[:len(state)])

res = sm.tsa.seasonal_decompose ( (data_df[state_name]) .fillna(0) ,freq=12)

pertussis_observed_state = res.observed
pertussis_seasonal_state = res.seasonal
pertussis_trend_state = res.trend

# Getting the observed, seasonal, trend.

#=======================================================================================================================
# An example of using ews_plot.

import ews
import ews_plot

#-----trend
x = np.array(pertussis_trend_state)
x[np.isnan(x)] = np.nanmean(x)

filename="./"+str(state_name)+"_Trend"+".pdf"

ews_df = ews.get_ews(x, windowsize=100, ac_lag=1)
ews_df["Time"] = np.arange(len(x))
signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

ews_plot.ews_plot (ews_df,signals,filename)

#-----seasonal
x = pertussis_seasonal_state.dropna().values
filename="./"+str(state_name)+"_Seasonal"+".pdf"

ews_df = ews.get_ews(x, windowsize=100, ac_lag=1)
ews_df["Time"] = np.arange(len(x))
signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

ews_plot.ews_plot (ews_df,signals,filename)
#------observed_log
x= np.log(pertussis_observed_state + 0.05).dropna().values
filename="./"+str(state_name)+"Log_observed"+".pdf"

ews_df = ews.get_ews(x, windowsize=100, ac_lag=1)
ews_df["Time"] = np.arange(len(x))
signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

ews_plot.ews_plot (ews_df,signals,filename)