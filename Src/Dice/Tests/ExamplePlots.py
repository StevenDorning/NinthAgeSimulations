import unittest
import numpy
import matplotlib.pyplot as plt

import Dice.Dice as Dice

class TestPlots(object):

    def __init__(self):

        self.plotIndex = 0

        self.PlotD6Distribution()

        self.PlotD12Distribution()

        self.Plot2D6Distribution()

        self.Plot3D6RemoveLowestDistribution()

    def DoSubPlot(self):

        plt.subplot(2,2,self.plotIndex)

        self.plotIndex += 1

    def PlotD6Distribution(self):

        self.DoSubPlot()

        numOfSides = 6

        numOfIterations = 10000

        myDice = Dice.Dice(numOfSides)

        results = [0] * numOfSides

        for i in range(numOfIterations):

            v = myDice.RollSingle()

            results[v-1] +=1

        x = range(1,numOfSides+1)

        plt.bar(
            x, results, 1/1.5, align='center'
        )

        plt.title("D6 Distribution")

    def PlotD12Distribution(self):

        self.DoSubPlot()

        numOfSides = 12

        numOfIterations = 10000

        myDice = Dice.Dice(numOfSides)

        results = [0] * numOfSides

        for i in range(numOfIterations):

            v = myDice.RollSingle()

            results[v-1] +=1

        x = range(1,numOfSides+1)

        plt.bar(
            x, results, 1/1.5, align='center'
        )

        plt.title("D12 Distribution")

    def Plot2D6Distribution(self):

        self.DoSubPlot()

        numOfSides = 6

        numOfIterations = 10000

        myDice = Dice.Dice(numOfSides)

        results = [0] * (numOfSides * 2 -1)

        for i in range(numOfIterations):

            v = myDice.SumMultipleDice(2)

            results[v-2] += 1

        x = range(2,numOfSides*2+1)

        plt.bar(
            x, results, 1/1.5, align='center'
        )

        plt.title("2D6 Distribution")

    def Plot3D6RemoveLowestDistribution(self):

        self.DoSubPlot()

        numOfSides = 6

        numOfIterations = 10000

        myDice = Dice.Dice(numOfSides)

        results = [0] * (numOfSides * 2 -1)

        for i in range(numOfIterations):

            v = myDice.SumMultipleDice(3, ignoreNLowest=1)

            results[v-2] += 1

        x = range(2,numOfSides*2+1)

        plt.bar(
            x, results, 1/1.5, align='center'
        )

        plt.title("3D6 (remove lowest)")

    def ShowAll(self):

        plt.show()

myPlot = TestPlots()

myPlot.ShowAll()