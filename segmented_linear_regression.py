import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from linear_fit import linear_fit #local function
#============================================ Segmented Linear Regression ==============================================
# this function is using in segmented_linear_regression function.
import numpy as np
def linear_fit( x , a1, b1, a2, b2, bp ):
    x = x.reshape(-1)
    def lf(xi):
        if(xi < x[bp]):
            return(a1*xi + b1)
        else:
            return(a2*xi + b2)

    return(np.array([lf(i) for i in x]))

#=======================================================================================================================
#input x,y
def piecewise(x,y):
    x = x.reshape(-1,1)
    y= y.reshape(-1,1)

    print("Len of X array is:",len(x))
    print("Len of Y array is:",len(y))

    model1 = LinearRegression()  # fit_intercept = False
    model2 = LinearRegression()  # fit_intercept = False
    s = -np.inf
    for i in range(1,len(x)):

        model1.fit(x[:i], y[:i])
        model2.fit(x[i:], y[i:])

        s1 = model1.score(x[:i],y[:i])
        s2 = model2.score(x[i:],y[i:])
        if(s1+s2 > s):
            s = s1+s2
            a1 = model1.coef_.reshape(-1)
            a2 = model2.coef_.reshape(-1)
            b1 = model1.intercept_
            b2 = model2.intercept_
            bp = i

    y_fit = linear_fit(x, a1, b1, a2, b2, bp)

    #print(y_fit)
    #print(y_fit[x < x[bp]])

    plt.plot(x.reshape(-1),y.reshape(-1),'b')

    plt.plot(x[x <x[bp]],y_fit[x < x[bp]],'r')
    plt.plot(x[x >=x[bp]],y_fit[x >=x[bp]],'r')

    return y_fit.reshape(-1) # Transfer the Horizantal to Vertical!
    #print(y_fit[bp])

    #plt.show()
#=======================================================================================================================

#simple example:
#input ()
'''
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15])
y = np.array([5, 7, 9, 11, 13, 15, 28.92, 42.81, 56.7, 70.59, 84.47, 98.36, 112.25, 126.14, 140.03])
piecewise(x,y)
'''

#============================= Test the Error =====================

import matplotlib.pyplot as plt ;
import numpy as np ;
import pandas as pd ;
import statsmodels.api as sm

from segmented_linear_regression import piecewise


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

#--------------------------------------------------Piece wise-----------------------------------------------------------

x = np.array(Time_Series[:len(pertussis_trend_state.dropna())])
y = np.array(pertussis_trend_state.dropna())

print(piecewise(x,y)) # The problem is not the piecewise ! (good news)