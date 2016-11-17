import timeit


def get_lychrel_numbers(boundary):
    counter = 0
    for number in range(1, boundary +1):
        if is_lychrel_number(number) : counter += 1
    return counter


def is_lychrel_number(number):
    flag = True
    for i in range(1, 51):
        reversed_number = get_reversed(number)
        if is_palindrome(number + reversed_number):
            flag = False
            break
        number = number + reversed_number
    return flag


def get_reversed(number):
    return int(str(number)[::-1])


def is_palindrome(number):
    number = str(number)
    flag = True
    i = 0
    while i <= int(len(number) / 2) and flag == 1:
        if number[i] != number[-(i+1)]:
            flag = False
        i += 1
    return flag


if __name__=='__main__':
    start = timeit.default_timer()

    print(get_lychrel_numbers(10000))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")