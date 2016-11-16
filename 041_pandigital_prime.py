import timeit


def get_pandigital_primes():
    digits = [1,2,3,4,5,6,7,8,9]
    pandigital_primes = []
    primes = get_primes(1, 7654321)
    for prime in primes:
        prime_in_list = []
        temp_prime = prime
        while temp_prime > 0:
            prime_in_list.append(temp_prime % 10)
            temp_prime = int(temp_prime / 10)
        prime_in_list.sort()
        temp_digits = digits[:len(prime_in_list)]
        if prime_in_list == temp_digits: pandigital_primes.append(prime)
    return max(pandigital_primes)


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

    print(get_pandigital_primes())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
