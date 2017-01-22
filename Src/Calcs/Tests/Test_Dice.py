import unittest
import Calcs.Dice as Dice


class TestDieRolls(unittest.TestCase):

    def setUp(self):

        self.standardDice = [2,4,6,8,10,12,20]

        self.numIterations = 10000

    def test_SingleDiceRoll(self):

        for n in self.standardDice:

            myDice = Dice.Dice(n)

            resultCount = {}

            for i in range(self.numIterations):

                myVal = myDice.RollSingle()

                self.assertIn(myVal, range(1,n,1))

                if myVal not in resultCount:
                    resultCount[myVal] = 0

                resultCount[myVal] += 1

            #Check to see we have all possible results
            #This isn't guranteed but we are using a lot of iterations so should happen

            self.assertEquals(sorted(resultCount.keys()), range(1,n+1))



    def test_SummedDiceRoll(self):

        for numSides in self.standardDice:

            myDice = Dice.Dice(numSides)

            resultCount = {}

            for numOfDiceToRoll in [1,2,3,4,5,6]:

                for i in range(self.numIterations):

                    myVal = myDice.SumMultipleDice(numOfDiceToRoll)

                    self.assertIn(myVal, range(numOfDiceToRoll, numOfDiceToRoll*numSides))

                    if myVal not in resultCount:
                        resultCount[myVal] = 0

                    resultCount[myVal] += 1

    def test_IgnoreDice(self):

        fakeResults = [1,1,2,3,4,5,6,7,9,20]

        myDice = Dice.Dice(20)

        self.assertEquals(myDice.RemoveDiceToIgnore(fakeResults,0,0), fakeResults)

        self.assertEquals(myDice.RemoveDiceToIgnore(fakeResults,1,0), [1,2,3,4,5,6,7,9,20])

        self.assertEquals(myDice.RemoveDiceToIgnore(fakeResults,3,0), [3,4,5,6,7,9,20])

        self.assertEquals(myDice.RemoveDiceToIgnore(fakeResults,1,2), [1,2,3,4,5,6,7])








if __name__ == '__main__':
    unittest.main()
