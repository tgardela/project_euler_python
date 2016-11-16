import timeit


def coin_sums_brute():
    coin_sum = 200
    ways = 0
    for a in range(coin_sum,-1, -200):
        for b in range(a,-1, -100):
            for c in range(b,-1,-50):
                for d in range(c,-1,-20):
                    for e in range(d,-1,-10):
                        for f in range(e,-1,-5):
                            for g in range(f,-1,-2):
                                ways +=1
    return ways


def coin_sums_not_brute():
    target = 200
    coinSizes = [1,2,5,10,20,50,100,200]
    ways = [0 for i in range(201)]
    ways[0] = 1

    for i in range(0, len(coinSizes)):
        for j in range(coinSizes[i], target+1):
            ways[j] += ways[j - coinSizes[i]]

    return ways[200]


if __name__=="__main__":
    for f in [coin_sums_brute(), coin_sums_not_brute()]:
        start = timeit.default_timer()

        print(f)

        stop = timeit.default_timer()
        print("Time: ", stop - start, " s")