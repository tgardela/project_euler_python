import timeit

def get_answer(howMany):
    return find_consecutive_numbers_in_list(find_numbers_with_n_dividers(howMany), howMany)


def find_consecutive_numbers_in_list(numbers, howMany):
    consecutive_numbers = []
    for n in range(0, len(numbers) + 1 - howMany):
        if numbers[n+3] + numbers[n+2] + numbers[n+1] + numbers[n] == 4 * numbers[n] + 6:
            consecutive_numbers.append((numbers[n],numbers[n+1], numbers[n+2], numbers[n+3]))
            break
    return consecutive_numbers


def find_numbers_with_n_dividers(numberOfDividers):
    return [x for x in range(210, 134500) if get_number_of_dividers(x) == numberOfDividers]


def get_number_of_dividers(number):
    return len([x for x in range(2, int(number / 2) + 1) if number % x == 0 and is_prime(x)])


def get_primes(max):
    return [x for x in range(1, max +1) if is_prime(x)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    start = timeit.default_timer()

    print(get_answer(4))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
