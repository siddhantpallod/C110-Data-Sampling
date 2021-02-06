import plotly.figure_factory as pf
import plotly.graph_objects as pg
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv('data.csv')

totaldata = df['average'].tolist()


def randomSetOfMeans(counter):
    dataset = []

    for i in range(0, counter):
        randomIndex = random.randint(0, len(totaldata))
        value = totaldata[randomIndex]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean


def showFig(meanList):
    df = meanList
    mean = statistics.mean(meanList)
    print("Mean is", mean)
    fig = pf.create_distplot([df], ['average'], show_hist=False)
    fig.show()


def main():
    meanList = []

    for i in range(0, 100):
        setOfMeans = randomSetOfMeans(100)
        meanList.append(setOfMeans)

    std = statistics.stdev(meanList)
    print(std)

    showFig(meanList)


main()
