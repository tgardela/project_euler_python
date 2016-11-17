import timeit


def find_longest_consecutive_prime_sum():
    primes = get_primes(1, 999999)
    sumOfPrimes = 0
    for prime in primes:
        if sumOfPrimes + prime > 1000000: break
        else:
            sumOfPrimes += prime
    for prime in primes:
        sumOfPrimes -= prime
        if is_prime(sumOfPrimes): break
    return sumOfPrimes


def get_primes(start, stop):
    return [n for n in range(start,stop) if is_prime(n)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

if __name__=='__main__':
    start = timeit.default_timer()

    print(find_longest_consecutive_prime_sum())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
