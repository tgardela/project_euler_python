import timeit
import decimal

def solution():
    # numbers =  getNumberFromFile()
    numbers = getSmall()
    findMinPathSum(numbers)



def findMinPathSum(numbers):
    lenN = len(numbers)
    sum = numbers[lenN-1][lenN-1]
    left = lenN - 1
    up = lenN - 1
    counter = 0
    while left > 0 and up > 0:
        if numbers[left - 1][up] < numbers[left][up - 1]:
            sum += numbers[left - 1][up]
            print numbers[left - 1][up]
            left -= 1
        else:
            sum += numbers[left][up - 1]
            print numbers[left][up - 1]
            up -= 1

        counter += 1
    print sum + numbers[0][0]


def getSmall():
    return [[131, 673, 234, 103, 18],
            [201, 96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524, 37, 331]]

def getNumberFromFile():
    numbers = []
    file = open('081_path_sums_two_ways.txt', 'r')
    for row in file:
        numbers.append([int(k) for k in row.split(',')])
    return numbers

if __name__=="__main__":
    start = timeit.default_timer()

    print solution()


    stop = timeit.default_timer()
    print "Time: ", stop - start, " s"
