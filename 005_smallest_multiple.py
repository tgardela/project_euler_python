import timeit


def smallest_multiple(end, step):
    dividers = [11,13,14,16,17,18,19,20]
    for number in range(step, end, step):
        if all(number % n == 0 for n in dividers):
            return number
    return None

if __name__=='__main__':
    start = timeit.default_timer()

    print(smallest_multiple(999999999, 2520))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")