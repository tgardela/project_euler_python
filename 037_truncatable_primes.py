import timeit


def get_both_side_truncatable_primes():
    primes = generate_primes(8, 999999)
    return sum([p for p in primes if is_left_truncatable(p) and is_right_truncatable(p)])


def generate_primes(start, stop):
    return [n for n in range(start, stop + 1) if is_prime(n)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def is_left_truncatable(number):
    flag = True
    for n in range(1, len(str(number)) + 1 ):
        if is_prime(number) and number > 10:
            tempNumber = str(number)[1:]
            number = int(tempNumber)
        elif is_prime(number): pass
        else: return False
    return flag


def is_right_truncatable(number):
    flag = True
    for n in range(1, len(str(number)) + 1):
        if is_prime(number):
            number = int(number / 10)
            flag = True
        else: return False
    return flag


if __name__ == '__main__':
    start = timeit.default_timer()

    print(get_both_side_truncatable_primes())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")