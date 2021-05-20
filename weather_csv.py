import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    """ for index, column_header in enumerate(header_row):
        print(index, column_header) """
    # # Get dates and high temperatures from this file.
    cities,highs, lows = [], [], []
    for row in reader:
        current_city = row[5]
        high = int(row[10])
        low = int(row[11])
        cities.append(current_city)
        highs.append(high)
        lows.append(low)
    # print(highs)

    # Plot the high temperatures.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(highs, c='red')
    ax.plot(cities, highs, c='red',  alpha=0.5)
    ax.plot(cities, lows, c='blue',  alpha=0.5)
    plt.fill_between(cities, highs, lows, facecolor='lightgreen', alpha=0.1)

    # Format plot.
    plt.title("Daily high and low temperatures, January 2016", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()