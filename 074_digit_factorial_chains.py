import timeit
from math import factorial


def solution():
    number_of_60_term_chains = 0

    for number in range(1000000):
        if get_chain_length(number) == 60:
            number_of_60_term_chains += 1

    return number_of_60_term_chains


def get_chain_length(number):
    numbers_in_chain = []
    x = get_factorial_sum(number)
    while x not in numbers_in_chain:
        numbers_in_chain.append(x)
        x = get_factorial_sum(x)
    return len(numbers_in_chain) + 1


def get_factorial_sum(number):
    number = [int(c) for c in str(number)]
    return sum([factorial(n) for n in number])


if __name__ == '__main__':
    start = timeit.default_timer()

    print(solution())

    # print(get_chain_length(78))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
