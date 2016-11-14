import timeit


def find_longest_sequence(limit):
    longest_sequence = 0
    longest_sequence_number = 0
    for number in range(2, limit):
        sequence_of_number = find_sequence(number)
        if sequence_of_number > longest_sequence:
            longest_sequence = sequence_of_number
            longest_sequence_number = number
    return "Number = " + str(longest_sequence_number) + " with sequence of: " + str(longest_sequence)


def find_sequence(start_number):
    counter = 1
    searched_number = start_number
    while searched_number != 1:
        if searched_number % 2 == 0:
            searched_number /= 2
        else:
            searched_number = 3 * searched_number + 1
        counter += 1
    return counter


if __name__=='__main__':
    start = timeit.default_timer()

    limit = 1000000
    print(find_longest_sequence(limit))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")