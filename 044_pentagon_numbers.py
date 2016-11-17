import timeit


def find_pentagonals():
    pentagonals = get_pentagonals()
    pentset = set(pentagonals)
    for i in pentagonals:
        for j in pentagonals:
            pent1 = i
            pent2 = j
            sPlus = set()
            sMinus1 = set()
            sMinus2 = set()
            sPlus.add(pent1 + pent2)
            sMinus1.add(pent2 - pent1)
            sMinus2.add(pent1 - pent2)
            if pentset.intersection(sPlus) and (pentset.intersection(sMinus1) or pentset.intersection(sMinus2)):
                return abs(pent2 - pent1)


def get_pentagonals():
    return [pentagonal(i) for i in range(1, 3500)]


def pentagonal(n):
    pentagonal = n * (3 * n - 1) / 2
    return pentagonal


if __name__=="__main__":
    start = timeit.default_timer()

    print(find_pentagonals())


    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")