import timeit

def get_factorial_digits_sum(number):
    factorial = get_factorial(number)
    return get_sum_of_numbers_digits(factorial)


def get_factorial(number):
    factorial = 1
    for f in range(1, number + 1):
        factorial *= f
    return factorial


def get_sum_of_numbers_digits(number):
    number = str(number)
    sum = 0
    for n in number:
        sum += int(n)
    return sum


if __name__=='__main__':
    start = timeit.default_timer()

    print(get_factorial_digits_sum(100))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")