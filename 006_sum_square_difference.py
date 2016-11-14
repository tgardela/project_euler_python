import timeit

def solution(max_number):
    squareOfSum = 0
    sumOfSquares = 0
    for number in range (1, max_number + 1):
        squareOfSum += number
        sumOfSquares += number * number
    return squareOfSum * squareOfSum - sumOfSquares


if __name__=='__main__':
    start = timeit.default_timer()

    print(solution(100))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")