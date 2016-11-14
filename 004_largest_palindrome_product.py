import timeit

def is_palindrome(string):
    decide=1
    i=0
    while i<=int(len(string)/2) and decide==1:
        if string[i]!=string[-(i+1)]:
            decide=0
        i+=1
    return decide

def largest_palindrome_product(start, stop):
    aux = 0
    for k in range(start,stop):
        for j in range(start,stop):
            if is_palindrome(str( j * k )) and j * k > aux:
                aux = j * k
    return aux

if __name__=='__main__':
    start = timeit.default_timer()

    print(largest_palindrome_product(101, 1000))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")

