import timeit


def prime_generator():
    result = 1
    n = 0
    while True:
        if is_Prime(n):
            result *= n
            if result > 1000000:
                result /= n
                break
        n +=1
    return result, n


def is_Prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


if __name__=="__main__":
    start = timeit.default_timer()

    print(prime_generator())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")