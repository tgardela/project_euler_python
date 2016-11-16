import timeit


def sum_of_all_non_abundant_numbers(limit):
    abundant_numbers = all_sums_of_abundant_numbers(limit)
    return sum([number for number in range(1, limit + 1) if number not in abundant_numbers]) #4179871


def all_sums_of_abundant_numbers(limit):
    abundant_numbers = all_abundant_numbers_list(limit)
    sums_of_abundant_numbers = []
    for number in abundant_numbers:
        for i in abundant_numbers:
            if i >= number and (number + i) < (limit + 1):
                sums_of_abundant_numbers.append(number + i)

    return sums_of_abundant_numbers


def all_abundant_numbers_list(limit):
    return [number for number in range(1, limit + 1) if numbers_divider_sum(number) > number]


def numbers_divider_sum(number):
    return sum([divider for divider in range(1, int(number /2) + 1) if number % divider == 0])


if __name__=='__main__':
    start = timeit.default_timer()

    print(sum_of_all_non_abundant_numbers(28123))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")