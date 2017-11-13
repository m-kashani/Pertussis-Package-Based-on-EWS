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

    plt.show()
#=======================================================================================================================

#simple example:
#input ()
'''
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15])
y = np.array([5, 7, 9, 11, 13, 15, 28.92, 42.81, 56.7, 70.59, 84.47, 98.36, 112.25, 126.14, 140.03])
piecewise(x,y)
'''