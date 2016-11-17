import timeit


def get_answer():
    return str(sum([x**x for x in range(1, 1001)]))[-10:]


if __name__ == '__main__':
    start = timeit.default_timer()

    print(get_answer())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
