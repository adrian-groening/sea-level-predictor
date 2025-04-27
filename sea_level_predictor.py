import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df)



    # Create scatter plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level')
    plt.title('Sea Level Rise Over Time')


    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']


    plt.scatter(x, y, c='white', edgecolors='black', linewidths=1, alpha=0.75)


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    linex = pd.Series(range(x.min(), 2050))
    liney = slope * linex + intercept
    plt.plot(linex, liney)
    plt.show()
    



    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()