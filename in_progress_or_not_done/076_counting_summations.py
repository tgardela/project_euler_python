import timeit


def count_summations(number):
    target = number
    ways = [ 0 for i in range(number + 1)]
    ways[0] = 1
    for i in range (1, number):
        for j in range (i, target + 1):
            ways[j] += ways[j - i]
    return ways[100]


if __name__=="__main__":
    start = timeit.default_timer()

    print(count_summations(100))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")