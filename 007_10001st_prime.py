import timeit

def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def find_nth_prime(nth_prime):
    which_prime = 0
    for number in range(1, 99999999):
        if is_prime(number):
            which_prime += 1
        if which_prime == nth_prime:
            return number

if __name__=='__main__':
    start = timeit.default_timer()

    print(find_nth_prime(10001))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
