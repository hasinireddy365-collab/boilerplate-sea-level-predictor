import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Best fit line, all data, through 2050
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series(range(1880, 2051))
    ax.plot(years, res.intercept + res.slope * years, 'r')

    # Best fit line, year 2000 onward, through 2050
    recent = df[df['Year'] >= 2000]
    res2 = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    years2 = pd.Series(range(2000, 2051))
    ax.plot(years2, res2.intercept + res2.slope * years2, 'green')

    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    plt.savefig('sea_level_plot.png')
    return plt.gca()