import timeit

# aabb bbcc ccdd ddee eeff ffaa

def fuckIt():
    return fivelevels()

def fivelevels():
    numbers = []
    for t in getTriangular():
        for a in range(100):
            n = str(int(t[2:] + '00') + a)
            if n in getSquares():
                f = fourLevels(n, getPentagonal(), getHexagonal(), getHeptagonal(), getOctagonal())
                f.append(t)
                numbers += f
            if n in getPentagonal():
                f = fourLevels(n, getSquares(), getHexagonal(), getHeptagonal(), getOctagonal())
                f.append(t)
                numbers += f
            if n in getHexagonal():
                f = fourLevels(n, getSquares(), getPentagonal(), getHeptagonal(), getOctagonal())
                f.append(t)
                numbers += f
            if n in getHeptagonal():
                f = fourLevels(n, getSquares(), getPentagonal(), getHexagonal(), getOctagonal())
                f.append(t)
                numbers += f
            if n in getOctagonal():
                f = fourLevels(n, getSquares(), getPentagonal(), getHexagonal(), getHeptagonal())
                f.append(t)
                numbers += f
    return numbers

def fourLevels(number, first, second, third, fourth):
    numbers = []
    for a in range(100):
        n = str(int(str(number[2:]) + '00')  + a)
        if n in first:
            t = threeLevels(n, second, third, fourth)
            t.append(n)
            numbers += t
        if n in second:
            t = threeLevels(n, first, third, fourth)
            t.append(n)
            numbers += t
        if n in third:
            t = threeLevels(n, first, second, fourth)
            t.append(n)
            numbers += t
        if n in fourth:
            t = threeLevels(n, first, second, third)
            t.append(n)
            numbers += t
    return numbers

def threeLevels(number, first, second, third):
    numbers = []
    for a in range(100):
        n = str(int(str(number[2:]) + '00')  + a)
        if n in first:
            s = twoLevels(n, second, third)
            s.append(n)
            numbers += s
        if n in second:
            s = twoLevels(n, first, third)
            s.append(n)
            numbers += s
        if n in third:
            s = twoLevels(n, first, second)
            s.append(n)
            numbers += s
    return numbers

def twoLevels(number, first, second):
    numbers = []
    for a in range(100):
        n = str(int(str(number[2:]) + '00')  + a)
        if n in first:
            t = oneLevel(n, second)
            t.append(n)
            numbers += t
        if n in second:
            t = oneLevel(n, first)
            t.append(n)
            numbers += t
    return numbers

def oneLevel(number, first):
    numbers = []
    for a in range(100):
        n = str(int(str(number[2:]) + '00')  + a)
        if n in first:
            for b in range(100):
                t = str(int(str(n[2:]) + '00')  + b)
                if t in getTriangular():
                    numbers += t
    return numbers



def getCyclic(number):
    pass

def getTriangular():
    triangles = [str((i * ( i + 1) / 2)) for i in range(1, 141) if 999 < (i * ( i + 1) / 2) < 10000]
    return triangles

def getSquares():
    squares = [str((i * i)) for i in range(1, 141) if 999 < (i * i) < 10000]
    return squares

def getPentagonal():
    pentagonals = [str((i * ( 3 * i - 1) / 2)) for i in range(1, 141) if 999 < (i * ( 3 * i - 1) / 2) < 10000]
    return pentagonals

def getHexagonal():
    hexagonals = [str((i * (2 * i - 1))) for i in range(1, 141) if 999 < (i * (2 * i - 1)) < 10000]
    return hexagonals

def getHeptagonal():
    heptagonals = [str((i * (5 * i - 3) / 2)) for i in range(1, 141) if 999 < (i * (5 * i - 3) / 2) < 10000]
    return heptagonals

def getOctagonal():
    octagonal = [str((i * (3 * i - 2))) for i in range(1, 141) if 999 < (i * (3 * i - 2)) < 10000]
    return octagonal

if __name__=="__main__":
    start = timeit.default_timer()

    print(fuckIt())
    # print getPermutation(8120)

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")


# def fuckIt():
#     triangles = getTriangulars()
#     squares = getSquares()
#     pentagonals = getPentagonal()
#     hexagonals = getHexagonal()
#     heptagonals = getHeptagonal()
#     octagonals = getOctagonal()
#     triangle = 0
#     square = 0
#     pentagonal = 0
#     hexagonal = 0
#     heptagonal = 0
#     octagonal = 0
#     for triangle in triangles:
#         print 't ', triangle
#         for a in xrange(100):
#             square = int(triangle[2:] + '00')  + a
#             if str(square) in squares:# or triangle in pentagonals or triangle in hexagonals or triangle in heptagonals or triangle in octagonals:
#                 print '\ts ', square
#                 for b in xrange(100):
#                     pentagonal = int(str(square)[2:] + '00') + b
#                     if str(pentagonal) in pentagonals:
#                         print '\t\tp ', pentagonal
#                         for c in xrange(100):
#                             hexagonal = int(str(pentagonal)[2:] + '00') + c
#                             if str(hexagonal) in hexagonals:
#                                 print '\t\t\thex ', hexagonal
#                                 for d in xrange(100):
#                                     heptagonal = int(str(hexagonal)[2:] + '00') + d
#                                     if str(heptagonal) in heptagonals:
#                                         print '\t\t\t\thep ', heptagonal
#                                         for e in xrange(100):
#                                             octagonal = int(str(heptagonal)[2:] + '00') + e
#                                             if str(octagonal) in octagonals:
#                                                 print '\t\t\t\t\to ', octagonal
#                                                 for f in xrange(100):
#                                                     if int(str(heptagonal)[:2] + '00') + f == triangle[:2]:
#                                                         break