import timeit


def find_products():
    numberToCheck = ''
    foundPandigitals = set()
    for multiplicant in range(2, 100):
        for multiplier in range(2, 10000):
            numberToCheck += str(multiplier) + str(multiplicant) + str(multiplicant * multiplier)
            if len(numberToCheck) == 9:
                numberToCheck = int(numberToCheck)
                if is_pandigital(numberToCheck):
                    foundPandigitals.add(multiplicant * multiplier)
            numberToCheck = ''
    return sum(foundPandigitals)


def is_pandigital(number):
    digits = [1,2,3,4,5,6,7,8,9]
    numberToCheck = []
    while number > 0:
        numberToCheck.append(number % 10)
        number = int(number / 10)
    numberToCheck.sort()
    if numberToCheck == digits[:len(numberToCheck)]: return True


if __name__=="__main__":
    start = timeit.default_timer()

    print(find_products())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")