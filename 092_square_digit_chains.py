import timeit


def get_count_of_89_enders():
    counter89 = 0
    for number in range(1, 10000000):
        if is_square_digit_89(number) == 89:
            counter89 += 1
    return counter89


def is_square_digit_89(number):
    while True:
        tempNumber = 0
        for c in str(number):
            tempNumber += int(c) ** 2
        number = tempNumber
        if number == 89:
            return 89
        elif number == 1:
            return 1


if __name__=="__main__":
    start = timeit.default_timer()

    print(get_count_of_89_enders())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")