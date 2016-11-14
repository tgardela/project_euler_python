import timeit

def find_triplet():
    for a in range (1, 999):
        for b in range(1, 998):
            c = 1000 - a - b
            if (a*a + b*b == c*c): return a*b*c

if __name__=="__main__":
    start = timeit.default_timer()

    print(find_triplet())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")