import timeit

def find_sum():
    sum = 0
    for number in read_numbers_from_file():
        sum += number
    return sum


def read_numbers_from_file():
    numbers = []
    f = open('013_large_sum.txt', 'r')
    for number in f:
        numbers.append(int(number))
    return numbers

if __name__=='__main__':
    start = timeit.default_timer()

    print(find_sum())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")