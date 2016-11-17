import timeit


def find_max_power_digit_sum():
    maxSum = 0
    for number in range(1, 100):
        for power in range(1, 100):
            current_sum = get_sum_of_digits(number ** power)
            if current_sum > maxSum:
                maxSum = current_sum
    return maxSum


def get_sum_of_digits(number):
    number = str(number)
    sum = 0
    for char in number:
        sum += int(char)
    return sum


if __name__ == '__main__':
    start = timeit.default_timer()

    print(find_max_power_digit_sum())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
