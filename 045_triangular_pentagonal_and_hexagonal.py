import timeit


def find_the_number():
    triangulars = []
    pentagonals = []
    hexagonals = []
    for i in range(285, 200000):
        triangulars.append(triangular(i))
        pentagonals.append(pentagonal(i - 120))
        hexagonals.append((hexagonal(i - 142)))
    triangulars = set(triangulars)
    pentagonals = set(pentagonals)
    hexagonals = set(hexagonals)

    return triangulars.intersection(pentagonals, hexagonals)


def triangular(n):
    triangular = n * (n + 1) / 2
    return triangular


def pentagonal(n):
    triangular = n * (3 * n - 1) / 2
    return triangular


def hexagonal(n):
    triangular = n * (2* n - 1)
    return triangular


if __name__=="__main__":
    start = timeit.default_timer()


    print(find_the_number())

    stop = timeit.default_timer()
    print ("Time: ", stop - start, " s")