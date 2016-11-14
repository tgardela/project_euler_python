import timeit

def find_path_number(grid_size):
    number_of_paths = 1
    for i in range (0,grid_size):
        number_of_paths *= (2 * grid_size) - i
        number_of_paths /= i + 1
    return number_of_paths

if __name__=='__main__':
    start = timeit.default_timer()

    grid_size = 20
    print(find_path_number(grid_size))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")