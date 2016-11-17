import timeit


def returnPossibleCode():
    codes = getFileFromPath("079_Passcode_derivation.txt")
    numbers = returnNumbersWithPlaces(codes)
    for i in xrange(len(numbers)):
        print i, " : ", numbers[i]



def calculatePassword(numbers):
    pass

def returnNumbersWithPlaces(codes):
    numbersWithPlaces = []
    for i in xrange(10):
        numbersWithPlaces.append(3*[0])

    for code in codes:
        counter = 0
        for c in code:
            numbersWithPlaces[int(c)][counter] += 1
            counter += 1
    return numbersWithPlaces

def getFileFromPath(path):
    codes = []
    file = open(path, 'r')
    for line in file:
        codes.append(line.rstrip().replace(' ',''))
    return codes

if __name__=="__main__":
    start = timeit.default_timer()


    returnPossibleCode()

    stop = timeit.default_timer()
    print "Time: ", stop - start, " s"
