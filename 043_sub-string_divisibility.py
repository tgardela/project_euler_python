import timeit


def permutate(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permutate(rest):
                res.append(seq[i:i+1] + x)
        return res


def get_sum_of_wanted_pandigitals():
    pandigitals = permutate('0123456789')
    wanted_pandigitals = []
    for number in pandigitals:
        number = str(number)
        if is_substring_divisible(number):
                wanted_pandigitals.append(int(number))
    return sum(wanted_pandigitals)


def is_substring_divisible(number):
    flag = False
    dividers = [0,2,3,5,7,11,13,17]
    if '0' not in number: number = '0' + number
    for i in range(1,8):
        tempNumber = number[i] + number[i+1] + number[i+2]
        tempNumber = int(tempNumber)
        if not tempNumber % dividers[i] == 0 :
            flag = False
            return flag
        else:
            flag = True
    return flag


def is_pandigital(number):
    digits = [0,1,2,3,4,5,6,7,8,9]
    for digit in number:
        tempNum = int(digit)
        if tempNum in digits: digits.remove(tempNum)
    if not digits: return True
    else: return False


if __name__ == '__main__':
    start = timeit.default_timer()

    print(get_sum_of_wanted_pandigitals())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
