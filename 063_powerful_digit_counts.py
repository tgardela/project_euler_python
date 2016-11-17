import timeit


def search_for_power_digits():
    powerDigits = []
    for number in range(1, 100):
        for power in range(1, 100):
            powerDigit = number ** power
            if get_number_of_digits(powerDigit) == power:
                powerDigits.append(powerDigit)
    return len(powerDigits)


def get_number_of_digits(number):
    return len(str(number))


if __name__ == '__main__':
    start = timeit.default_timer()

    print(search_for_power_digits())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
