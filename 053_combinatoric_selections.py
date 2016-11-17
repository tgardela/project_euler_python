import timeit


def get_combinations():
    counter = 0
    for n in range(1, 101):
        for r in range (1, 101):
            combi = get_factorial(n) / ((get_factorial(r)) * get_factorial(n - r))
            if combi > 1000000: counter += 1
    return counter


def get_factorial(boundary):
    factorial = 1
    for f in range(1, boundary + 1):
        factorial *= f
    return factorial


if __name__ == '__main__':
    start = timeit.default_timer()

    print(get_combinations())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
