import pandas as pd
data_df = pd.read_csv('pertussis.51.12.csv')

Dates = data_df [ ["YEAR","MONTH"] ]
time = Dates['YEAR'].astype(str) + "-" + Dates['MONTH'].astype(str) + "-01"
time = pd.to_datetime(time , format = '%Y-%m-%d')

Y = data_df["YEAR"]
M = data_df["MONTH"]
New_M = M / 12.0   # one way
Time_Series = Y.values + New_M.values

state_name = "California"

import statsmodels.api as sm
import numpy as np

state = ( data_df[state_name] )

state.index = pd.DatetimeIndex(time[:len(state)])

# for filling with average! ---------------------  # can be better later ...
data_df_np_array = data_df[state_name].values
average = np.nanmean(data_df_np_array)
#------------------------------------------------
#12 months
res = sm.tsa.seasonal_decompose ( (data_df[state_name]) .fillna(average) ,freq=12)
#calculate the requered signals to plot as pdf
pertussis_observed_state = res.observed
pertussis_seasonal_state = res.seasonal
pertussis_trend_state = res.trend

#============================================ Segmented Linear Regression ==============================================
from segmented_linear_regression import piecewise
#=======================================================================================================================

import ews
import ews_plot

name = input("(t/trend o/observe lt/logtrend lo/logobserve) please enter the name : ")

if (name=='t'):

    #to do piecewise on Trend
    trend_t = np.array(Time_Series[:len(pertussis_trend_state.dropna())])
    trend_y = np.array(pertussis_trend_state.dropna())

    piecewise_fited_trend = piecewise(trend_t, trend_y)

    #pdf for trend
    filename="Cal_using_mean/"+str(state_name)+"_Trend"+".pdf"

    ews_df = ews.get_ews(trend_y, windowsize=100, ac_lag=1)
    ews_df["Time"] = trend_t
    signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

    ews_df["piecewise_fited"] = piecewise_fited_trend #Added Now

    ews_plot.ews_plot (ews_df,signals,filename,"trend")

elif (name=='lt'):

    # to do Piecewise on LOG trend
    log_trend_t = np.array(Time_Series[:len(pertussis_trend_state.dropna())])  # trend_t
    log_trend_y = np.log(np.array(pertussis_trend_state.dropna()))  # trend_y = np.array()

    piecewise_fited_log_trend = piecewise(log_trend_t, log_trend_y)

    #pdf for log trend
    filename="Cal_using_mean/"+str(state_name)+"_LogTrend"+".pdf"

    ews_df = ews.get_ews(log_trend_y, windowsize=100, ac_lag=1)
    ews_df["Time"] = log_trend_t
    signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

    ews_df["piecewise_fited"] = piecewise_fited_log_trend #Added Now

    ews_plot.ews_plot (ews_df,signals,filename,"Log_trend")

elif (name=='o'):

    # to do piecewise on Observed
    observed_t = np.array(Time_Series[:len(pertussis_observed_state.dropna())])
    observed_y = np.array(pertussis_observed_state.dropna())

    piecewise_fited_observed = piecewise(observed_t, observed_y)

    #pdf for observed
    filename="Cal_using_mean/"+str(state_name)+"_observed"+".pdf"

    ews_df = ews.get_ews(observed_y, windowsize=100, ac_lag=1)
    ews_df["Time"] = observed_t
    signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

    ews_df["piecewise_fited"] = piecewise_fited_observed #Added Now

    ews_plot.ews_plot (ews_df,signals,filename,"observed")

elif(name=="lo"):

    #to do piecewise on LOG observed
    log_observed_t = np.array(Time_Series[:len(pertussis_observed_state.dropna())])
    log_observed_y = np.log(np.array(pertussis_observed_state.dropna())+0.01) #observed_y = np.array---.dropna()

    piecewise_fited_log_observed = piecewise(log_observed_t,log_observed_y)

    #pdf for log observed
    filename="Cal_using_mean/"+str(state_name)+"log_Observed"+".pdf"

    ews_df = ews.get_ews(log_observed_y, windowsize=100, ac_lag=1)
    ews_df["Time"] = log_observed_t
    signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time","coefficient_of_variation","kurtosis","skewness"]

    ews_df["piecewise_fited"] = piecewise_fited_log_observed #Added Now

    ews_plot.ews_plot (ews_df,signals,filename,"log_observed")

else:
    print("your input for name is not defined. you should use lt/lo/t/o instead.")