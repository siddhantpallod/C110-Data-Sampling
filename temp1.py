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


def randomSetOfMeans(counter):
    dataset = []

    for i in range(0,counter):
        randomIndex = random.randint(0,len(totaldata))
        value = totaldata[randomIndex]  
        dataset.append(value)
    
    mean = statistics.mean(dataset)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(meanList)
    print("Mean is", mean)
    fig = pf.create_distplot([df],['temp'], show_hist = False)
    fig.add_trace(pg.Scatter(x = [mean, mean], y = [0,1], mode = 'lines', name = 'MEAN'))
    fig.show()


def main():
    meanList = []

    for i in range(0,1000):
        setOfMeans = randomSetOfMeans(100)
        meanList.append(setOfMeans)
    
    std = statistics.stdev(meanList)
    print(std)
    
    showFig(meanList)

main()

# relationship between total std and std of sampling mean distribution = std of sampling mean = 
# std of total data by sqrt of (number of data in each sample)
# std of sampling mean distribution is also called as standard error of the mean (SE)
