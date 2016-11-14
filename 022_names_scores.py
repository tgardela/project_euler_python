import timeit

def count_scores_names():
    total_score = 0
    index = 0
    names = names_from_file()
    for name in names:
        index += 1
        total_score += score_name(name) * (names.index(name) + 1)
    return total_score


def names_from_file():
    f = open('022_names_scores.txt', 'r')
    file = f.readline()
    file = file.replace("\"","")
    names = file.split(',')
    names.sort()
    return names


def score_name(name):
    name_score = 0
    letters_value = { 'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,
                     'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    for letter in name:
        if letter not in letters_value:
            print("Letter does not match:\t", letter)
        name_score += letters_value.get(letter)
    return name_score


if __name__=='__main__':
    start = timeit.default_timer()

    print(count_scores_names())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")