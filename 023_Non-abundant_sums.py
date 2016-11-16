import timeit

def FindSumOfAllNonAbundantNumbers(limit):
    abundantNumbers = FindAllSumsOfAbundatnNumbers(limit)
    sumOfNonAbundantNumbers = 0
    for number in xrange(1, limit + 1):
        if number not in abundantNumbers:
            sumOfNonAbundantNumbers += number
    print sumOfNonAbundantNumbers               #4179871

def FindAllSumsOfAbundatnNumbers(limit):
    abundantNumbers = FindAllAbundantNumbersAndPutThemInAList(limit)
    sumsOfAbundantNumbers = []
    for number in abundantNumbers:
        for i in abundantNumbers:
            if i >= number and (number + i) < (limit + 1):
                sumsOfAbundantNumbers.append(number + i)
    return sumsOfAbundantNumbers

def FindAllAbundantNumbersAndPutThemInAList(limit):
    abundantNumbers = []
    for number in xrange(1, limit + 1):
        if ReturnNumbersDividerSum(number) > number:
            abundantNumbers.append(number)
    return abundantNumbers

def ReturnNumbersDividerSum(number):
    dividerSum = 0
    for divider in xrange (1, number /2 + 1):
        if number % divider == 0:
            dividerSum += divider
    return dividerSum

if __name__=='__main__':
    start = timeit.default_timer()

    FindSumOfAllNonAbundantNumbers(28123)

    stop = timeit.default_timer()
    print "Time: ", stop - start, " s"