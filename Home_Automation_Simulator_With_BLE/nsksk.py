import random
from itertools import count
import pandas as pd
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
   
    x = data['time_as_x_value']
    y1 = data['temperature_as_y_value']
    y2 = data['humidity_as_y_value']

    plt.cla()

    plt.plot(x, y1, label='Temp_Data')
    plt.plot(x, y2, label='Humidity_Data')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate,interval = 1000)

plt.tight_layout()
plt.show()
time.sleep(1)