import timeit

def count_circular_primes():
    cyclicPrimes = get_cyclic_primes()
    return len(cyclicPrimes)


def get_cyclic_primes():
    return [i for i in range(2, 1000000) if is_prime(i) and is_cyclic(i)]


def is_cyclic(prime):
    prime = str(prime)
    flag = False
    if len(prime) == 1: return True
    for i in range(1, len(prime)):
        if is_prime(int(prime[1:] + prime[:1])):
            prime = prime[1:] + prime[:1]
        else:
            flag = False
            break
        flag = True
    return flag


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


if __name__=="__main__":
    start = timeit.default_timer()

    print(count_circular_primes())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")