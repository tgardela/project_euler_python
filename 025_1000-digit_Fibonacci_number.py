import timeit


def fibonacchi(limit):
    previous = 1
    next = 1
    temp = 0
    term = 2
    while str(temp).__len__() < limit:
        term += 1
        temp = previous + next
        previous = next
        next = temp
    return term


if __name__=="__main__":
    start = timeit.default_timer()

    limit = 1000
    print(fibonacchi(limit))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")