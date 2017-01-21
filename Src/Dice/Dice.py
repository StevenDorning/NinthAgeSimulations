import random



class Dice(object):

    def __init__(self, numSides):

        self.__numSides = numSides

        #this randomises to the current time
        random.seed()

    def RollSingle(self):

        return random.randrange(1,self.__numSides+1)

    def SumMultipleDice(self, numberToRoll, ignoreNLowest= 0, ignoreNHighest = 0):

        results = []

        for i in range(numberToRoll):

            results.append( self.RollSingle() )

        prunedResults = self.RemoveDiceToIgnore(results, ignoreNLowest, ignoreNHighest)

        return sum(prunedResults)

    def RemoveDiceToIgnore(self, allDice, ignoreNLowest, ignoreNHighest):

        tmp = sorted(allDice)

        if ignoreNHighest + ignoreNLowest >= len(allDice):
            raise ValueError , "The number of dice to ignore is greater than the total number of dice rolled."

        result =  tmp[ignoreNLowest:  len(allDice)  - ignoreNHighest]

        return result



class SingleDiceGroup(object):

    def __init__(self, numSides):

        self.__die = Dice(numSides)

    def __IsSuccesful(self, value, successValue, successIsHigh):

        if successIsHigh:
            return value >= successValue
        else:
            return value <= successValue

    def __ShouldIReRollDice(self, value, successValue, successIsHigh,reRollFailures, reRollSuccess, specificValuesToReRoll ):

        return reRollFailures is not None and not self.__IsSuccesful(value, successValue, successIsHigh) or \
                reRollSuccess is not None and self.__IsSuccesful(value, successValue, successIsHigh) or \
                specificValuesToReRoll is not None and value in specificValuesToReRoll


    def RollDiceAndGetNumberOfSuccesses(self, numberToRoll, successValue, successIsHigh=True,  reRollFailures = False, reRollSuccess=False, specificValuesToReRoll=None):

        numberOfSuccesses = 0

        for d in range(numberToRoll):
            v = self.__die.RollSingle()

            if self.__ShouldIReRollDice(v,successValue, successIsHigh, reRollFailures, reRollSuccess, specificValuesToReRoll):
                v = self.__die.RollSingle()

            if self.__IsSuccesful(v, successValue, successIsHigh):
                numberOfSuccesses += 1








