import timeit


def find_value():
    cons = get_champernownes_constant()
    valueToFind = int(cons[1]) * int(cons[10]) * int(cons[100]) * int(cons[1000]) * int(cons[10000]) * int(cons[100000]) * int(cons[1000000])
    return valueToFind


def get_champernownes_constant():
    constant = '.'
    for i in range(1, 1000001):
        constant += str(i)
    return constant



if __name__ == '__main__':
    start = timeit.default_timer()

    print(find_value())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")