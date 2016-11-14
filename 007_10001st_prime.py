import timeit

def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def find_nth_prime(nthPrime):
    whichPrime = 0
    for number in range(1, 99999999):
        if is_prime(number):
            whichPrime += 1
        if whichPrime == nthPrime:
            return number

if __name__=='__main__':
    start = timeit.default_timer()

    print(find_nth_prime(10001))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
