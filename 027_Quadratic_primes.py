import timeit


def get_maximum_number_of_primes():
    numberOfPrimes = 0
    aA = 0
    bB= 0
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            tempMax = get_maximum_number_of_primes_for_given_A_and_B(a, b)
            if tempMax > numberOfPrimes:
                numberOfPrimes = tempMax
                aA = a
                bB = b
    return aA * bB


def get_maximum_number_of_primes_for_given_A_and_B(a, b):
    numberOfPrimes = 0
    while True:
        if is_prime(numberOfPrimes**2 + a*numberOfPrimes + b): numberOfPrimes += 1
        else: break
    return numberOfPrimes


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

if __name__=="__main__":
    start = timeit.default_timer()

    print(get_maximum_number_of_primes())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")