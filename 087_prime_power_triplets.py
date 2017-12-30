import timeit


def get_number_of_primes(limit):
    primes = get_primes(7070)
    primes_squared = [p**2 for p in primes]
    primes_tripled = [p**3 for p in primes]
    primes_quadrupled = [p**4 for p in primes]

    numbers = set()
    for i in primes_quadrupled:
        if i > limit: break
        for j in primes_tripled:
            if i + j > limit: break
            for k in primes_squared:
                if i + j + k > limit: break
                numbers.add(i + j + k)
    return len(numbers)


def get_primes(limit):
    return [n for n in range(limit) if is_prime(n)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


if __name__=="__main__":
    start = timeit.default_timer()

    print(get_number_of_primes(50000000))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")