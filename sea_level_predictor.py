import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10,10))
    ax.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    lreg1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y1 = [x1 * lreg1.slope + lreg1.intercept for x1 in range(df['Year'].min(), 2051)]
    
    ax.plot(range(df['Year'].min(), 2051), y1)

    # Create second line of best fit
    filtered_years = df[(df['Year'] <= 2050) & (df['Year'] >= 2000)]['Year']
    filtered_sea_level = df[(df['Year'] <= 2050) & (df['Year'] >= 2000)]['CSIRO Adjusted Sea Level']
    
    lreg2 = linregress(filtered_years, filtered_sea_level)
    y2 = [x2 * lreg2.slope + lreg2.intercept for x2 in range(filtered_years.min(), 2051)]
    
    ax.plot(range(filtered_years.min(), 2051), y2)

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()