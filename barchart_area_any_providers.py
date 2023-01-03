'''
Makes a barchart for number of providers per area type.
'''

import matplotlib.pyplot as plt
import pandas as pd

def bar_plot(log_scale):
    data = pd.read_csv('area_any_providers.csv')

    df = pd.DataFrame(data)
    X = list(df.iloc[:, 1])
    Y = list(df.iloc[:, 2])

    if log_scale:
        plt.yscale("log")
    
    plt.bar(X, Y, color='g')

    plt.title("Number of providers that accepted Medicare in 2019 per area")
    plt.xlabel("Area")
    if log_scale:
        plt.ylabel("Log of Number of Providers")
    else:
        plt.ylabel("Number of Providers")

    plt.show()
