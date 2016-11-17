import timeit


def calculate():
    return (28433 * (2 ** 7830457) + 1) % 10000000000


if __name__=="__main__":
    start = timeit.default_timer()

    print(calculate())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")