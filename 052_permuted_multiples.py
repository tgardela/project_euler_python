import timeit


def get_smallest_permuted_multiple():
    permuted_multiples = [num for num in range(12, 999999) if are_multiple_digits_the_same(num)]
    return min(permuted_multiples)


def are_multiple_digits_the_same(number):
    multiples = set('.'.join(sorted(str(mult * number))) for mult in range(1, 7))

    if len(multiples) > 1:
        return False
    else:
        return True


if __name__ == '__main__':
    start = timeit.default_timer()

    print(get_smallest_permuted_multiple())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
