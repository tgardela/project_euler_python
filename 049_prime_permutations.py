import timeit


def get_searched_primes():
    cos = []
    for number in range(1000, 10000):
        if is_prime(number):
            for i in range(1,4500):
                if is_prime(number + i) and is_prime(number + i + i) and number + i + i < 10000:
                    if are_digits_the_same(number, number + i, number + i +i):
                        cos.append([number, number + i, number + i + i])
    return cos


def is_prime(number):
    flag = True
    for i in range(2, number):
        if number % i != 0: pass
        else:
            flag = False
            break
    return flag


def are_digits_the_same(number, number2, number3):
    digits1 = number_to_digit_list(number)
    digits2 = number_to_digit_list(number2)
    digits3 = number_to_digit_list(number3)
    if digits1 == digits2 == digits3:
        return True


def number_to_digit_list(number):
    digits = []
    while number > 0:
        digits.append(number % 10)
        number = int(number / 10)
    return set(digits)


if __name__=="__main__":
    start = timeit.default_timer()

    print(get_searched_primes())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")