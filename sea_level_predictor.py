import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df)



    # Create scatter plot


    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']


    plt.scatter(x, y, c='white', edgecolors='black', linewidths=1, alpha=0.75)


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    linex = pd.Series(range(x.min(), 2051))
    liney = slope * linex + intercept
    plt.plot(linex, liney)
    

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']

    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(x_recent, y_recent)

    # Predict from 2000 to 2050
    line_x_recent = pd.Series(range(2000, 2051))
    line_y_recent = slope_recent * line_x_recent + intercept_recent

    # Plot
    plt.scatter(x, y)  # scatter of original data
    plt.plot(linex, liney, color='red', label='Best Fit Line (All Data)')
    plt.plot(line_x_recent, line_y_recent, color='green', label='Best Fit Line (2000-present)')




    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()