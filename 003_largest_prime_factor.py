import timeit


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def find_largest_prime_factor(number_to_check):
    prime_factors = []
    number = 1
    actively_changing_variable = number_to_check
    while number < actively_changing_variable:
        if number_to_check % number == 0 and is_prime(number):
            prime_factors.append(number)
            actively_changing_variable = number_to_check / number
        number += 1
    return max(prime_factors)



if __name__=="__main__":
    start = timeit.default_timer()
    number = 600851475143

    print(find_largest_prime_factor(number))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
