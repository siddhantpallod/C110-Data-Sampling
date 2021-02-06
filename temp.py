import plotly.figure_factory as pf
import plotly.graph_objects as pg
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv('temp.csv')

totaldata = df['temp'].tolist()

totalmean = statistics.mean(totaldata)
print(totalmean)

totalstd = statistics.stdev(totaldata)
print(totalstd)

dataset = []

for i in range(0,1000):
    randomIndex = random.randint(0,len(totaldata))
    value = totaldata[randomIndex]  
    dataset.append(value)

mean = statistics.mean(dataset)
std = statistics.stdev(dataset)
print(mean)
print(std)

fig = pf.create_distplot([totaldata],['temp'], show_hist = False)
fig.add_trace(pg.Scatter(x = [totalmean, totalmean], y = [0,1], mode = 'lines', name = 'MEAN'))
fig.show()