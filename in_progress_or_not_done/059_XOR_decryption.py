import timeit


def tryKeysOnFile():
    keys = getPropableEcryptionKeys()
    message = getFileContentsAsList('059_XOR_decryption.txt')
    result = open('059_XOR_wynik.txt', 'w')
    counter = 0
    for key in keys:
        decryptedMessage =''
        decryptedMessageAsList = decryptTheMessage(message, key)
        for c in decryptedMessageAsList:
            decryptedMessage += str(c)
        if checkForEnglishWords(decryptedMessage):
            counter += 1
            result.write(decryptedMessage + '\n')
            return countSumOfLettersInASCII(decryptedMessage), '\tfor\t', decryptedMessage


def getPropableEcryptionKeys():
    keys = []
    fromList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    fromListASCII = [ord(x) for x in fromList]
    for k1 in fromListASCII:
        for k2 in fromListASCII:
            for k3 in fromListASCII:
                keys.append([k1,k2,k3])
    return keys


def getFileContentsAsList(filePathAndName):
    file = open(filePathAndName, 'r')
    for row in file:
        row = row.rstrip('\n')
        numbers = [int(k) for k in row.split(',')]
    return numbers


def decryptTheMessage(message, keyAsList):
    decryptedMessage = [] + [0]*(len(message))
    for c1 in range(0, len(message) + 2 - 2, 3):
        decryptedMessage[c1] = (int(message[c1]) ^ keyAsList[0])
    for c1 in range(1, len(message) + 2 - 2, 3):
        decryptedMessage[c1] = (int(message[c1]) ^ keyAsList[1])
    for c1 in range(2, len(message) + 2 - 2, 3):
        decryptedMessage[c1] = (int(message[c1]) ^ keyAsList[2])
    return transformASCIIToLetters(decryptedMessage)


def transformASCIIToLetters(toTransform):
    letters = []
    for digit in toTransform:
        letters.append(chr(digit))
    return letters


def checkForEnglishWords(message):
    if 'the' in message and 'and' in message and 'in' in message: return True
    else: return False


def countSumOfLettersInASCII(message):
    asciiSumOfMessage = 0
    for char in message:
        asciiSumOfMessage += ord(char)
    return asciiSumOfMessage


def transformLettersToASCII(toTransform):
    keyInASCII = []
    for letter in toTransform:
        keyInASCII.append(ord(letter))
    return keyInASCII

if __name__ == '__main__':
    start = timeit.default_timer()

    print(tryKeysOnFile())

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")
