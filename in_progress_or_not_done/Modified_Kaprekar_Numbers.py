import timeit


def get_kaprekalnumbers(s, f):
    return [i for i in range(s, f) if is_kaprekar_number(i)]


def is_kaprekar_number(number):
    if number == 1: return True
    numberS = str(number * number)
    if int(numberS) < 9: return False
    lenNS = len(numberS)

    for i in range(lenNS):
        tN1 = numberS[0:i+1]
        tN2 = numberS[i+1:lenNS]
        if tN2 == '':
            tN2 = 0
            return False

        if int(tN1) + int(tN2) == number:
            return True
    return False


if __name__=="__main__":
    start = timeit.default_timer()

    A = [[7,10]]

    print(get_kaprekalnumbers(1, 100))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")