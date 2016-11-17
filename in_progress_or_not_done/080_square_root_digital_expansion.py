import timeit
import decimal


def solution():
    sqrts = get_irrational_square_roots()
    return sum([get_digital_sum(sqrt) for sqrt in sqrts])


def get_irrational_square_roots():
    sqrts = []
    for i in range(0,100):
        decimal.getcontext().prec = 102
        sqrt = decimal.Decimal(i).sqrt()
        if sqrt % 1:
            sqrts.append(sqrt)
    return sqrts


def get_digital_sum(sqrt):
    sqrt = str(sqrt).replace('.', '')[:100]
    lenS = len(sqrt)
    sum = 0
    for i in range(0, lenS):
        sum += int(sqrt[i])
    return sum


def solution2():
    decimal.getcontext().prec = 102
    L, d, s = 100, 100, 0
    p = pow(10, d-1)

    for z in range(2, L):
        q = decimal.Decimal(z).sqrt()
        s += sum(int(c) for c in str(q * p)[:d]) if  q % 1 != 0 else 0

    return s


if __name__=="__main__":
    for f in [solution, solution2]:
        start = timeit.default_timer()

        print(f())

        stop = timeit.default_timer()
        print("Time: ", stop - start, " s")