import numpy
import matplotlib.pyplot as plt

import Calcs.Dice as Dice

class RunPlots(object):

    def __init__(self):

        self.plotIndex = 1

        self.numIterations = 100000

        for n in [6,10,12,20]:

            self.Plot1DNDistribution(n)

            self.Plot2DNDistribution(n)

            self.Plot3DNRemoveLowestDistribution(n)

            self.Plot3DNRemoveHighestDistribution(n)


    def DoSubPlot(self):

        plt.subplot(4,4,self.plotIndex)

        self.plotIndex += 1

    def Plot1DNDistribution(self, numSides):

        print "Calculating 1D" + str(numSides)

        self.DoSubPlot()

        myDice = Dice.Dice(numSides)

        results = [0] * numSides

        for i in range(self.numIterations):

            v = myDice.RollSingle()

            results[v-1] +=1

        x = range(1,numSides+1)

        plt.bar(
            x, results, 1/1.5, align='center'
        )

        plt.title("D" + str(numSides) + " Distribution")


    def Plot2DNDistribution(self, numSides):

        print "Calculating 2D" + str(numSides)

        self.DoSubPlot()

        myDice = Dice.Dice(numSides)

        results = [0] * (numSides * 2 -1)

        for i in range(self.numIterations):

            v = myDice.SumMultipleDice(2)

            results[v-2] += 1

        x = range(2,numSides*2+1)

        plt.bar(
            x, results, 1/1.5, align='center'
        )

        plt.title("2D" + str(numSides) + " Distribution")

    def Plot3DNRemoveLowestDistribution(self, numSides):

        print "Calculating 3D" + str(numSides) + " (ignore lowest)"

        self.DoSubPlot()

        myDice = Dice.Dice(numSides)

        results = [0] * (numSides * 2 -1)

        for i in range(self.numIterations):

            v = myDice.SumMultipleDice(3, ignoreNLowest=1)

            results[v-2] += 1

        x = range(2,numSides*2+1)

        plt.bar(
            x, results, 1/1.5, align='center'
        )

        plt.title("3D" + str(numSides)+ " (remove lowest)")

    def Plot3DNRemoveHighestDistribution(self, numSides):

        print "Calculating 3D" + str(numSides) + " (ignore lowest)"

        self.DoSubPlot()

        myDice = Dice.Dice(numSides)

        results = [0] * (numSides * 2 - 1)

        for i in range(self.numIterations):
            v = myDice.SumMultipleDice(3, ignoreNHighest=1)

            results[v - 2] += 1

        x = range(2, numSides * 2 + 1)

        plt.bar(
            x, results, 1 / 1.5, align='center'
        )

        plt.title("3D" + str(numSides) + " (remove highest)")

    def ShowAll(self):

        plt.show()

myPlot = RunPlots()

myPlot.ShowAll()