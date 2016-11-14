import timeit

def find_sum_of_amicable_numbers(limit):
    return sum([n for n in range(1, limit + 1) if sum_of_dividers(sum_of_dividers(n)) == n and sum_of_dividers(n) != n])


def sum_of_dividers(number):
    return sum([divider for divider in range(1, int(number/2) + 1) if number % divider == 0])


if __name__=='__main__':
    start = timeit.default_timer()

    print(find_sum_of_amicable_numbers(10000))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")