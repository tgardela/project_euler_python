import timeit

def find_sum_of_all_double_base_palindroms():
    return sum([number for number in range(1, 1000000) if is_palindromic(str(number)) and is_palindromic(str(bin(number)))])


def is_palindromic(number):
    if number[0] == '0' and number[1] == 'b':
        number = number [2:]
    flag = True
    index = 0
    while index <= int(len(number)/2) and flag == True:
        if number[index] != number[-(index + 1)]:
            flag = False
        index += 1
    return flag

if __name__ == '__main__':
    start = timeit.default_timer()

    print(find_sum_of_all_double_base_palindroms())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
