import timeit

def getSumOfPrimeGeneratingIntegers():
    counter = 0
    sumOfPrimeGeneratingIntegers = 1
    for number in xrange(2, 1000, 4):     #100000000
        if isPrimeGeneratingInteger(number):
            sumOfPrimeGeneratingIntegers += number
            counter += 1
            print number
    print "Counter: ", counter
    return sumOfPrimeGeneratingIntegers

def isPrimeGeneratingInteger(number):
    if not isPrime(number + 1): return False
    else:
        dividers = [div for div in xrange(1, int(number ** 0.5) + 1) if number % div == 0]
        for div in dividers:
            if isPrime(div + number / div): continue
            else: return False
        return True

def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

if __name__=="__main__":
    start = timeit.default_timer()

    print getSumOfPrimeGeneratingIntegers()

    # print isPrimeGeneratingInteger(11637238)


    stop = timeit.default_timer()
    print "Time: ", stop - start, " s"