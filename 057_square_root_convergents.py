import timeit


def getNumberOfFractionsWithNominatorLongerThanDenominator(expansions):
    counter = 0
    nOld = 3
    dOld = 2
    for i in range(1, expansions + 1):
        if does_numerator_have_more_digits_than_denominator(nOld, dOld): counter += 1
        nNew = nOld + 2*dOld
        dNew = nOld + dOld
        nOld = nNew
        dOld = dNew
    return counter


def does_numerator_have_more_digits_than_denominator(num, den):
    if len(str(num)) > len(str(den)):
        return True
    else:
        return False


if __name__=='__main__':
    start = timeit.default_timer()

    print(getNumberOfFractionsWithNominatorLongerThanDenominator(1000))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")