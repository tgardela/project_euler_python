import timeit


def find_max_solutions():
    perimeter_with_max_solutions = 0
    temp = 0
    for perimeter in range(119, 1000):
        x = get_number_of_valid_solutions(perimeter)
        if temp < x:
            perimeter_with_max_solutions = perimeter
            temp = x
    return perimeter_with_max_solutions


def get_number_of_valid_solutions(perimeter):
    number_of_solutions = 0
    list_of_side_configurations = []
    for side1 in range (1, int(perimeter / 2) + 1):
        for side2 in range (1, int(perimeter / 4) + 1):
            side3 = perimeter - side1 - side2
            if is_triangle_right_angular(side1, side2, side3):
                temp_list = [side1, side2, side3]
                temp_list.sort()
                if not temp_list in list_of_side_configurations:
                    list_of_side_configurations.append(temp_list)
                    number_of_solutions += 1
    return number_of_solutions


def is_triangle_right_angular(side1, side2, side3):
    if side3*side3 == side1*side1 + side2*side2:
        return True
    else:
        return False


if __name__ == '__main__':
    start = timeit.default_timer()

    print(find_max_solutions())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")