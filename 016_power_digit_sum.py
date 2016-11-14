import timeit

def power_digit_sum(power):
    return sum([int(i) for i in str(2**power)])

#sum(map(int,str(2**1000))

if __name__=='__main__':
    start = timeit.default_timer()

    power = 1000
    print(power_digit_sum(power))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")