import timeit


def get_prime_sum():
    return sum(generate_primes(2000000))


def generate_primes(max):
    return [n for n in range(1, max) if is_prime(n)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


if __name__=="__main__":
    start = timeit.default_timer()

    print(get_prime_sum())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")