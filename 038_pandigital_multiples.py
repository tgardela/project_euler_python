import timeit

def generate_pandigital_multiples():
    temp_pan_mul = ''
    pandigital_multiples_list = []
    for number in range(1, 99999):
        for multipl in range(1, 10):
            temp_pan_mul += str(multipl * number)
            if len(temp_pan_mul) == 9 and is_pandigital(int(temp_pan_mul)):
                pandigital_multiples_list.append(int(temp_pan_mul))
                temp_pan_mul = ''
            elif len(temp_pan_mul) > 9:
                temp_pan_mul = ''
                break
    return max(pandigital_multiples_list)


def is_pandigital(number):
    digits = [1,2,3,4,5,6,7,8,9]
    numberToCheck = []
    while number > 0:
        numberToCheck.append(number % 10)
        number = int(number / 10)
    numberToCheck.sort()
    if numberToCheck == digits[:len(numberToCheck)]: return True


if __name__ == '__main__':
    start = timeit.default_timer()

    print(generate_pandigital_multiples())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
