# Plot each year petussis data ! Maybe something can be learned in future.

#=======================================================================================================================
# I am trying to write a code to estimate the missing number (NaN) nad then check it with the real data.
# Just on 1959 - 1960 - 1961
import pandas as pd
import matplotlib.pyplot as plt

#================================== Reading the data and Making Time Series ============================================

# Getting the data.

data_df = pd.read_csv('pertussis.51.12.csv')

# Making the time Series.

Dates = data_df [ ["YEAR","MONTH"] ]
time = Dates['YEAR'].astype(str) + "-" + Dates['MONTH'].astype(str) + "-01"
time = pd.to_datetime(time , format = '%Y-%m-%d')

data_1959 = data_df [data_df["YEAR"] == 1959]
print(data_1959)

data_1960 = data_df [data_df["YEAR"] == 1960]
print(data_1960)

data_1961 = data_df [data_df["YEAR"] == 1961]
print(data_1961)

data_1962 = data_df [data_df["YEAR"] == 1962]
print(data_1962)

print((data_1959))

# Making the time Series.
Dates = data_df [ ["YEAR","MONTH"] ]
time = Dates['YEAR'].astype(str) + "-" + Dates['MONTH'].astype(str) + "-01" #For each state ?
time = pd.to_datetime(time , format = '%Y-%m-%d')

# ploting the time Series
plt.suptitle("California pertussiss 1959-1960-1961-1962")
plt.plot(data_1959["California"],"or")
plt.plot(data_1960["California"],"og")
plt.plot(data_1961["California"],"ob")
plt.plot(data_1962["California"],"oy")

plt.show()