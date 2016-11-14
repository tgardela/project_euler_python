import timeit

def multiples_of_3_and_5():
    return sum(set(range(0, 1000, 3))|set(range(0, 1000, 5)))


def multiples_of_3_and_5_on_sets():
    return sum(set(range(0, 1000, 3))|set(range(0, 1000, 5)))


if __name__=="__main__":

    for function in (multiples_of_3_and_5, multiples_of_3_and_5_on_sets):
        start = timeit.default_timer()
        print("Function: ", function)
        print(function())

        stop = timeit.default_timer()
        print("Time: ", stop - start, " s")