import timeit

#   n - side length
#   corner for n is (start to end):
#   n * n,  (n-1)*n + 1,    (n-2)*n + 2,    (n-3)* + 3


def find_sum_of_diagonals():
    diagonalSum = 1
    for n in range(3,1002,2):
        diagonalSum = diagonalSum + (n * n) + ((n-1)*n + 1) +((n-2)*n + 2) + ((n-3)*n + 3)
    return diagonalSum


if __name__ == '__main__':
    start = timeit.default_timer()

    print(find_sum_of_diagonals())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
