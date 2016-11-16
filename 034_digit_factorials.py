import timeit
import math


def get_sum_of_digit_factorials():
    return sum([number for number in range(3, 9999999) if get_factorials_sum_of_number(number) == number])


def get_factorials_sum_of_number(number):
    factorialSum = 0
    for n in range(1, len(str(number)) + 1):
        factorialSum += math.factorial(int(number % 10))
        number /= 10
    return factorialSum


if __name__ == '__main__':
    start = timeit.default_timer()

    print(get_sum_of_digit_factorials())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
