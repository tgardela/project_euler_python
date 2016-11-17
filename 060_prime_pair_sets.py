import timeit

def get_answer():
    primes = get_primes(9999)
    lenP = len(primes)
    minSum = 5 * max(primes)

    for a in range(0, lenP):
        if 5 * primes[a] >= minSum: break
        for b in range(a + 1, lenP):
            if primes[a] + 4 * primes[b] >= minSum: break
            if are_two_primes_a_prime([primes[b], primes[a]]):
                for c in range(b + 1, lenP):
                    if primes[a] + primes [b] + 3 * primes[c] >= minSum: break
                    if are_two_primes_a_prime([primes[a], primes[c]]) and are_two_primes_a_prime([primes[b], primes[c]]):
                        for d in range(c + 1, lenP):
                            if primes[a] + primes [b] + primes[c] + 2 * primes[d] >= minSum: break
                            if (are_two_primes_a_prime([primes[a], primes[d]]) and
                                are_two_primes_a_prime([primes[b], primes[d]]) and
                                are_two_primes_a_prime([primes[c], primes[d]])):
                                for e in range(d + 1, lenP):
                                    if primes[a] + primes[b] + primes[c] + primes[d] + primes[e] >= minSum: break
                                    if (are_two_primes_a_prime([primes[a], primes[e]]) and
                                    are_two_primes_a_prime([primes[b], primes[e]]) and
                                    are_two_primes_a_prime([primes[c], primes[e]]) and
                                    are_two_primes_a_prime([primes[d], primes[e]])):
                                        tempSum = primes[a] + primes[b] + primes[c] + primes[d] + primes[e]
                                        if tempSum < minSum:
                                            minSum = tempSum
    return minSum


def are_two_primes_a_prime(primes):
    primes = [str(x) for x in primes]
    prime1 = primes[0] + primes[1]
    prime2 = primes[1] + primes[0]
    if is_prime(int(prime1)) and is_prime(int(prime2)):
        return True
    else:
        return False


def get_permutation(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in get_permutation(rest):
                res.append(seq[i:i+1] + x)
        return res


def get_primes(boundary):
    return [x for x in range(1, boundary) if is_prime(x)]


def is_prime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True


if __name__=="__main__":
    start = timeit.default_timer()

    print(get_answer())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
