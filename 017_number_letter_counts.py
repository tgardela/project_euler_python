import timeit


def sum_of_letters(maxNumber):
    sumOfLetters = 0
    for number in range(1, maxNumber + 1):
        sumOfLetters += letter_counter(number)
    return(sumOfLetters)


def letter_counter(number):
    number = str(number)
    counter = 0
    if len(number) == 1:
        counter += count_one_digit_numbers(number)
    elif len(number) == 2:
        counter += count_two_digit_numbers(number)
    elif len(number) == 3:
        counter += count_three_digit_numbers(number)
    elif len(number) == 4:
        counter += count_four_digit_numbers(number)
    return counter


def count_one_digit_numbers(number):
    ones = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
            '9': 'nine'}
    return len(ones[number])


def count_two_digit_numbers(number):
    counter = 0
    twos = {'10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
            '16': 'sixteen',
            '17': 'seventeen', '18': 'eighteen', '19': 'nineteen', '20': 'twenty', '30': 'thirty', '40': 'forty',
            '50': 'fifty',
            '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}
    if number in twos:
        counter += len(twos[number])
    else:
        counter += count_tennish_numbers(number[0]) + count_one_digit_numbers(number[1])
    return counter


def count_three_digit_numbers(number):
    counter = 0
    andConnector = len('and')
    hundredConnector = len('hundred')
    twos = {'10':'ten', '11':'eleven','12':'twelve','13':'thirteen','14':'fourteen','15':'fifteen','16':'sixteen',
            '17':'seventeen','18':'eighteen','19':'nineteen','20':'twenty','30':'thirty','40':'forty','50':'fifty',
            '60':'sixty','70':'seventy','80':'eighty','90':'ninety'}
    counter += count_one_digit_numbers(number[0]) + hundredConnector
    cos = number[1] + number[2]
    if cos == '00':
        pass
    elif number[1] == '0':
        counter = counter + andConnector + count_one_digit_numbers(number[2])
    elif cos in twos:
        counter = counter + andConnector + count_two_digit_numbers(cos)
    else:
        counter = counter + andConnector + count_tennish_numbers(number[1]) + count_one_digit_numbers(number[2])
    return counter


def count_four_digit_numbers(number):
    return count_one_digit_numbers(number[0]) + len('thousand')


def count_tennish_numbers(number):
    twosForOnes = {'2':'twenty','3':'thirty','4':'forty','5':'fifty','6':'sixty','7':'seventy','8':'eighty','9':'ninety'}
    return len(twosForOnes[number])


if __name__=='__main__':
    start = timeit.default_timer()

    number = 1000
    print(sum_of_letters(number))

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")

