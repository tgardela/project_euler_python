import timeit


def concealed_square():
    for i in range(1111119999, 1999999999):
        n = str(i * i)
        if len(n)==19 and n[0]=='1' and n[2]=='2' and n[4]=='3' and n[6]=='4' and n[8]=='5' and n[10]=='6'\
            and n[12]=='7' and n[14]=='8' and n[16]=='9' and n[18]=='0':
            return i


if __name__=="__main__":
    start = timeit.default_timer()

    print(concealed_square())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")