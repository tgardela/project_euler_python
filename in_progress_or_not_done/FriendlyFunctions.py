import timeit


def get_factorial(boundary):
    factorial = 1
    for f in range(1, boundary + 1):
        factorial *= f
    return factorial


def get_file_from_path(path):
    hands = []
    file = open(path, 'r')
    for line in file:
        hands.append(line.rstrip().replace(' ',''))
    return hands


def get_file_from_url_generator(url):
    from urllib.request import urlopen
    file_url = url #'https://projecteuler.net/project/resources/p054_poker.txt'
    return (line.split() for line in urlopen(file_url))


def get_reversed(number):
    return str(number)[::-1]


def get_permutation(seq):
    if seq is not str:
        seq = str(seq)
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in get_permutation(rest):
                res.append(seq[i:i+1] + x)
        return res


def get_XOR(val1, val2):
    return val1 ^ val2


def is_palindrome(number):
    number = str(number)
    flag = True
    i=0
    while i <= int(len(number) / 2) and flag == 1:
        if number[i] != number[-(i+1)]:
            flag = False
        i += 1
    return flag


def is_pandigital(number):
    digits = [0,1,2,3,4,5,6,7,8,9]
    for digit in number:
        tempNum = int(digit)
        if tempNum in digits: digits.remove(tempNum)
    if not digits: return True
    else: return False


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

if __name__=='__main__':
    start = timeit.default_timer()



    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
