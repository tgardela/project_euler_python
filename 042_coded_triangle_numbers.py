import timeit


def compare_word_letter_sums_to_triangular_numbers():
    triangulars = generate_triangular_numbers()
    word_letter_sums = sum_word_letters()
    triangular_words = 0
    for sum in word_letter_sums:
        if sum in triangulars: triangular_words += 1
    return triangular_words


def sum_word_letters():
    words = read_words_to_list()
    letters = get_letter_as_a_number()
    sums_of_word_letters = []
    for word in words:
        sumOfLetters = 0
        for letter in word:
            sumOfLetters += letters[letter]
        sums_of_word_letters.append(sumOfLetters)
    return sums_of_word_letters


def read_words_to_list():
    file = open('042_coded_triangle_numbers.txt', 'r')
    words = file.read().replace('"', '').split(',')
    return words


def generate_triangular_numbers():
    return [int(0.5*number*(number + 1)) for number in range(1, 30) ]


def get_letter_as_a_number():
    letters = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,
               'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
    return letters


if __name__ == '__main__':
    start = timeit.default_timer()

    print(compare_word_letter_sums_to_triangular_numbers())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
