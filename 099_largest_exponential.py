import timeit
from math import log


def solution():
    numbers = (get_number_from_file())
    max_number = 0
    max_i = 0
    for i in range(len(numbers)):
        base = log(numbers[i][0])
        exp = numbers[i][1]
        temp_number = base * exp
        if temp_number > max_number:
            max_number = temp_number
            max_i = i
    return max_i + 1


def get_number_from_file():
    numbers = []
    file = open('099_largest_exponential.txt', 'r')
    for row in file:
        row = row.rstrip('\n')
        temp_number = [int(k) for k in row.split(',')]
        numbers.append(temp_number)
    return numbers


if __name__ == '__main__':
    start = timeit.default_timer()

    print(solution())

    # print(get_chain_length(78))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
