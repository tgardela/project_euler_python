import timeit


def get_sum_of_fifth_power_digit_numbers():
    power = 5
    return sum([i for i in range(2, 1000000) if is_sum_of_digits__an_nth_power(i, power)])


def is_sum_of_digits__an_nth_power(number, power):
    tempNumber = number
    sum_of_digits_powers = 0

    for n in range(1, str(number).__len__() + 1):
        temp = tempNumber % 10
        tempNumber = int(tempNumber / 10)
        sum_of_digits_powers += temp**power

    if sum_of_digits_powers == number:
        return True
    return False


if __name__=="__main__":
    start = timeit.default_timer()

    print(get_sum_of_fifth_power_digit_numbers())

    stop = timeit.default_timer()
    print ("Time: ", stop - start, " s")

