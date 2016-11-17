import timeit
import fractions
from math import sqrt


def solution():
    oneIntegers = 0
    triangles = []
    for l in range(12, 1500000, 2):
        if ((l / 10) or (l / 100) or (l / 1000) or (l / 10000) or (l / 100000)) in triangles:
            continue
        if getnumberOfSides(l) == 1:
            oneIntegers += 1
            triangles.append(l)
    return oneIntegers


def getnumberOfSides(l):
    sides = []
    for i in range(int(l / 4), int(l / 4) + 1):
        for j in range(i + 1, int(l / 3) + 1):
            k = l - i - j
            if i*i + j*j == k*k:
               sides.append([i, j, k])
            if len(sides) > 1:
                break
    return len(sides)


def solution2():
    limit = 1500000
    triangles = [0] * (limit + 1)
    result = 0
    mlimit = int(sqrt(limit / 2))

    for m in range(2, mlimit):
        for n in range(1, m):
            if ((n + m) % 2) == 1 and fractions.gcd(n,m) == 1:
                a = m * m + n * n
                b = m * m - n * n
                c = 2 * m * n
                p = a + b + c
                while p <= limit:
                    triangles[p] += 1
                    if triangles[p] == 1:
                        result += 1
                    if triangles[p] == 2:
                        result -= 1
                    p += a + b + c
    c = 0
    for t in triangles:
        if t == 1:
            c += 1
    return c


if __name__=="__main__":
    start = timeit.default_timer()

    print(solution())
    print("bbb")
    print(solution2())

    # print getnumberOfSides(1200000)

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
