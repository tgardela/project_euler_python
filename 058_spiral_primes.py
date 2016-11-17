import timeit


def calculate_ratio(minRatio):
    ratio = 1.0
    sideLength = 3
    number_of_diagonal_numbers = 1.0
    primesSum = 0
    while ratio > 0.1:
        primesSum += float(get_sum_of_primes_per_layer(sideLength))
        number_of_diagonal_numbers += 4.0
        ratio = float(primesSum) / number_of_diagonal_numbers
        sideLength += 2
    return sideLength - 2


def get_sum_of_primes_per_layer(n):
    primes_per_layer = 0
    if is_prime(n*n) : primes_per_layer += 1
    if is_prime((n-1)*n + 1) : primes_per_layer += 1
    if is_prime((n-2)*n + 2) : primes_per_layer += 1
    if is_prime((n-3)*n + 3) : primes_per_layer += 1
    return primes_per_layer


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    start = timeit.default_timer()

    print(calculate_ratio(0.1))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
