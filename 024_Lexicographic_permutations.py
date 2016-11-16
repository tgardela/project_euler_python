import timeit


def permutate(digits, which_one):
    digits = list(digits)
    wanted_number = []
    for x in range(1, digits.__len__() + 1):
        temp_factorial = get_factorial(digits)
        combinations_per_digit_per_factorial = temp_factorial / digits.__len__()
        reminder = 0
        for digit in digits:
            reminder += combinations_per_digit_per_factorial
            if digits.__len__() == 1:
                digits.append(digits[0])
            else:
                if reminder >= which_one:
                    wanted_number.append(digit)
                    digits.remove(digit)
                    which_one -= reminder - combinations_per_digit_per_factorial
                    break
    return int(''.join(wanted_number))


def get_factorial(number):
    factorial = 1
    for x in range(1, number.__len__() + 1):
        factorial *= x
    return factorial


if __name__=="__main__":
    start = timeit.default_timer()

    print(permutate("0123456789", 1000000))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")