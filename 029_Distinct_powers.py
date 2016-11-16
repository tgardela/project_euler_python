import timeit

def getDistinctPowersTerms():
    distinct_power_terms = set()
    for a in range(2, 101):
        for b in range (2, 101):
            distinct_power_terms.add(a**b)
    return len(distinct_power_terms)

if __name__ == '__main__':
    start = timeit.default_timer()

    print(getDistinctPowersTerms())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
