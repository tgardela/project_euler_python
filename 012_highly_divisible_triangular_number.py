import timeit
import math

def find_triangular_number(number_of_dividors):
    number = 0
    i = 1
    while number_of_dividers(number) < number_of_dividors:
        number += i
        i += 1
    return number

def number_of_dividers(current_triangular_number):
    counter = 0
    square_root = math.sqrt(current_triangular_number)
    for number in range(2, int(square_root)+1):
        if current_triangular_number % number == 0:
            counter += 2
        if (square_root * square_root == number):
            counter -= 1
    return counter + 2

if __name__=='__main__':
    start = timeit.default_timer()

    print(find_triangular_number(500))

    stop = timeit.default_timer()
    print("Time: ", stop - start)