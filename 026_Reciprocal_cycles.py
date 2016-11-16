import timeit

def get_value_for_the_longest_cycle():
    number = 0
    max_cycle_length = 0
    for d in range(1, 1000):
        if get_recurring_cycle_length(d) > max_cycle_length:
            number = d
            max_cycle_length = get_recurring_cycle_length(d)
    return number

def get_recurring_cycle_length(d):
    cycle = []
    number = (1.0/7) * 10
    for i in range(1, d + 1):
        number = int(number) * 10
        if number in cycle:
            break
        else:
            cycle.append(number)
            number = float(number) % d
    return len(cycle)

if __name__=="__main__":
    start = timeit.default_timer()

    print(get_value_for_the_longest_cycle())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")