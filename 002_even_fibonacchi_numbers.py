import timeit


def fibonacci_evens(max_value):
    first = 1
    second = 2
    i = 0
    sum = 0
    while first < max_value:
        if first % 2 == 0:
            sum += first
        buf = first
        first = second
        second = buf + first
        i += 1
    return sum


#not part of solution
def fibonacci_recursion(x):
    if x < 2:
        return x
    else:
        return fibonacci_recursion(x - 1) + fibonacci_recursion(x - 2)


if __name__=="__main__":
    start = timeit.default_timer()
    max_value = 4000000

    print("Function: ", fibonacci_evens)
    print(fibonacci_evens(max_value))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")