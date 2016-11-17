import timeit


def find_smallest_odd_composite():
    primes = get_primes(1, 9999)
    odd_numbers_which_are_not_primes = find_odd_numbers_which_are_not_primes()
    for number in odd_numbers_which_are_not_primes:
        if not is_number_a_sum_of_prime_and_square(number, primes):
            return number


def find_odd_numbers_which_are_not_primes():
    return [number for number in range(9, 9999, 2) if not is_prime(number)]


def is_number_a_sum_of_prime_and_square(number, primes):
    flag = False
    for prime in primes:
        for to_square in range(1, 50):
            result = prime + 2 * to_square ** 2
            if result > number: break
            if number == result:
                flag = True
                return flag
    return flag


def get_primes(start, stop):
    return [n for n in range(start,stop) if is_prime(n)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    start = timeit.default_timer()

    print(find_smallest_odd_composite())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
