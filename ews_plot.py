import matplotlib.pyplot as plt

#Plot EWS and scaled EWS
def ews_plot(df, signals,
                 filename="./notes/decision_function.pdf", title=None):
    '''
    Plot EWS
    :param df: pandas.dataframe or dict with columns/entries named: Time, timeseries and all EWS listed in signals
    :param signals: list of EWS to be plotted
    :param filename: name of output file
    :param title: title for figure. No title shown if None
    :return: returns matplotlib figure
    '''

    plt.style.use('seaborn-darkgrid')
    # plt.rcParams.update({'figure.autolayout': True})

    fig, axes = plt.subplots(len(signals) + 1, 1, figsize=(6, 10), sharex=False, sharey=False)
    # add a big axes, hide frame
    fig.add_subplot(1, 1, 1, frameon=False)
    #  hide tick and tick label of the big axes
    plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
    plt.grid(False)
    plt.xlabel("time", labelpad=20)

    if (title != None):
        plt.title(title, y=1.02)
    fig.tight_layout(pad=2, w_pad=0.5, h_pad=0.5)

    t = df["Time"]

    axes[0].plot(t, df["timeseries"])
    axes[0].locator_params(nbins=3, axis='y')
    axes[0].set_xlim(min(t),max(t))
    axes[0].set_xticklabels([])
    axes[0].set_title("time series", loc="left", fontsize=12)
    for j, signal in enumerate(signals):
        x = df[signal]
        axes[j + 1].plot(t, x)
        axes[j+1].set_xlim(min(t), max(t))
        axes[j + 1].locator_params(nbins=3, axis='y')
        axes[j + 1].set_title(signal, loc="left", fontsize=12)
        if (j != len(signals)-1):
            axes[j + 1].set_xticklabels([])


        else:
            for tick in axes[j + 1].get_xticklabels():
                tick.set_rotation(45)
    if(filename != None):
        fig.savefig(filename, format='pdf')
    return(fig)

'''
#Example:
import numpy as np

#Replace with correct data:
x = np.random.random(300)

import ews
ews_df = ews.get_ews(x, windowsize=100, ac_lag=1)

#Replace this with correct time from data:
ews_df["Time"] = np.arange(len(x))

signals = ["variance","mean","index_of_dispersion","autocorrelation","decay_time",
          "coefficient_of_variation","kurtosis","skewness"]

ews_plot(ews_df,signals,filename="./test.pdf")
'''
