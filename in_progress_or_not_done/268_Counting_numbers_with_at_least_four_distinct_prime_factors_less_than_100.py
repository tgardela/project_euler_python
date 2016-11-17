import timeit
import itertools
from FriendlyFunctions import isPrime

def solution():
    primes = getPrimes()
    numberCounter = 0
    i = 0
    while i < (10**16L + 1):
        divisibles = getDivisibles(i)
        counter = 0
        for d in divisibles:
            if d in primes:
                counter += 1
            if counter == 4:
                numberCounter += 1
                break
        i += 1
    return numberCounter

def getDivisibles(number):
    divisibles = []
    for i in xrange(1, number/2):
        if number % i ==0:
            divisibles.append(i)
    return divisibles

def getPrimes():
    primes = []
    for i in xrange(0, 100):
        if isPrime(i):
            primes.append(i)
    return primes

if __name__=="__main__":
    start = timeit.default_timer()

    print solution()


    stop = timeit.default_timer()
    print "Time: ", stop - start, " s"
