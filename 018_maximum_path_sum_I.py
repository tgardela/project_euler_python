import timeit

def get_max_sum():
    numbers = get_number_from_file()
    numbers.reverse()
    for level in range(0, len(numbers) - 1):
        temp_level = []
        for index in range(0, len(numbers[level]) - 1):
            temp_level.append(get_sum_of_triangle(numbers[level + 1][index],numbers[level][index], numbers[level][index + 1]))
        numbers[level + 1] = temp_level
    return temp_level


def get_sum_of_triangle(a, b, c):
    return a + max(b, c)


def get_number_from_file():
    numbers = []
    file = open('018_maximum_path_sum_I.txt', 'r')
    for row in file:
        row = row.rstrip('\n')
        temp_number = [int(k) for k in row.split(' ')]
        numbers.append(temp_number)
    return numbers

if __name__=='__main__':
    start = timeit.default_timer()

    print(get_max_sum())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")