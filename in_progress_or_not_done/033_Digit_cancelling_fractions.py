import timeit


def findSmallestDenominatorOfTrivialFractionsProduct():
    nonTrivialFractions = findNonTrivialFractions()
    sumOfFractions = []
    for num in range(0, len(nonTrivialFractions)):
        sumOfFractions.append(float(nonTrivialFractions[num][0])/float(nonTrivialFractions[num][1]))


    return sum(sumOfFractions)

def findNonTrivialFractions():
    nonTrivialFractions = []
    for numerator in range(10, 100):
        for denominator in range (10, 100):
            if isNonTrivialFraction(numerator, float(denominator)):
                nonTrivialFractions.append([numerator, denominator])
    return nonTrivialFractions

def isNonTrivialFraction(numerator, denominator):
    numeratorRest = int(numerator) % 10
    denominatorRest = int(denominator) / 10
    tempNumerator = int(numerator) / 10
    tempDenominator = str(denominator)
    tempDenominator = tempDenominator[1:]
    tempDenominator = float(tempDenominator)
    nonMatter = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    if numerator in nonMatter or denominator in nonMatter or numerator >= denominator: return False
    elif (numeratorRest == denominatorRest) and ((numerator / denominator) == (tempNumerator / tempDenominator)): return True
    else: return False

if __name__=="__main__":
    start = timeit.default_timer()

    print(findSmallestDenominatorOfTrivialFractionsProduct())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")