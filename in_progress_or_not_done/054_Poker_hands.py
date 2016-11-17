import timeit
from collections import Counter
from urllib.request import urlopen

def countWins(): #ok
    player1WinsCount = 0
    games = dividePlayerHands(getFileFromPath("054_poker_hands.txt"))
    player1 = games[0]
    player2 = games[1]
    for game in range(0, len(player1)):
        if didPlayer1Win(player1[game], player2[game]): player1WinsCount += 1
    print("Player1 won ", player1WinsCount, " times out of", len(games[0]))

def didPlayer1Win(player1Hand, player2Hand):
    if getValueOfHand(player1Hand) > getValueOfHand(player2Hand): return True
    else: return False

def getValueOfHand(hand):
    # values = {i:j for i,j in enumerate('23456789TJQKA',start = 2)}

    hand = sortCards(hand)

    #przy powielanych kartach zrobic liczenie wartosci

    if isRoyalFlush(hand):#ok
        print("royalflush")
        return 1000 + getSuitValue(hand)
    elif isStraightFlush(hand):#ok
        print("straightflush")
        return 900 + getSuitValue(hand)
    elif isFourOfAKind(hand): #ok
        print("four of a kind")
        return 800 + getMaxCardValue(hand) + getSuitValue(hand) + getFourOfAKindValue(hand)
    elif isFullHouse(hand): #ok
        print("fullhouse")
        return 700 + getFullHouseValue(hand)
    elif isFlush(hand):#ok
        print("flush")
        return 600 + getSuitValue(hand) + getMaxCardValue(hand)
    elif isStraight(hand):#ok
        print("straight")
        return 500 + getMaxCardValue(hand)
    elif isThreeOfAKind(hand):#ok
        print("three ")
        return 400 + getMaxCardValue(hand) + getThreeOfAKindValue(hand)
    elif isTwoPairs(hand):#dodac zeby sprawdzal ktore 2 pary wyzsze, a potem ktora wolna karta jest wyzsza
        print("two pairs")
        return 300
    elif isOnePair(hand):#ok
        print("OnePair")
        return 200 + getOnePairValue(hand) + getMaxValueOfOnePair(hand)
    else:#ok
        "only highcard"
        return getMaxCardValue(hand)

def changeHandIntoList(hand):
    cards = []
    for h in range(0, 10, 2):
        cards.append(hand[h]+hand[h+1])
    return cards

def sortCards(hand):
    hand = changeHandIntoList(hand)
    counter = len(hand)/2 +1
    while counter > 0:
        # print
        for card in range(0, 4):
            # print "getCardValue(hand[card])", getCardValue(hand[card])
            # print "getCardValue(hand[card+1])", getCardValue(hand[card+1])
            if getCardValue(hand[card]) > getCardValue(hand[card+1]):
                a ,b = hand[card], hand[card+1]
                hand[card], hand[card+1] = b, a
        counter -= 1
    hand = ''.join(hand)
    return hand

def getSuitValue(hand):
    if hand[1] == 'S':
        return 1
    elif hand[1] == 'D':
        return 2
    elif hand[1] == 'H':
        return 3
    elif hand[1] == 'C':
        return 4

def getCardValue(card):
    values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    return values[card[0]]

def getMaxCardValue(hand):
    return getCardValue(hand[8])

def getFourOfAKindValue(hand):
    if (getCardValue(hand[2]) == getCardValue(hand[4]) \
            and getCardValue(hand[4]) == getCardValue(hand[6])\
            and getCardValue(hand[6]) == getCardValue(hand[8])):
        return getCardValue(hand[2])
    elif (getCardValue(hand[0]) == getCardValue(hand[2]) \
            and getCardValue(hand[2]) == getCardValue(hand[4])\
            and getCardValue(hand[4]) == getCardValue(hand[6])):
        return getCardValue(hand[0])

def getFullHouseValue(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2]) and getCardValue(hand[2]) == getCardValue(hand[4]))\
            and (getCardValue(hand[6]) == getCardValue(hand[8])):
        return 3 * getCardValue(hand[0]) + 2 * getCardValue(hand[6])
    elif (getCardValue(hand[2]) == getCardValue(hand[4]) and getCardValue(hand[4]) == getCardValue(hand[6]))\
            and (getCardValue(hand[0]) == getCardValue(hand[8])):
        return 3 * getCardValue(hand[2]) + 2 * getCardValue(hand[0])
    elif (getCardValue(hand[4]) == getCardValue(hand[6]) and getCardValue(hand[6]) == getCardValue(hand[8]))\
            and (getCardValue(hand[0]) == getCardValue(hand[2])):
        return 3 * getCardValue(hand[4]) + 2 * getCardValue(hand[0])

def getThreeOfAKindValue(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2]) and getCardValue(hand[2]) == getCardValue(hand[4])):
        return getCardValue(hand[0])
    elif (getCardValue(hand[2]) == getCardValue(hand[4])and getCardValue(hand[4]) == getCardValue(hand[6])):
        return getCardValue(hand[2])
    elif (getCardValue(hand[4]) == getCardValue(hand[6])and getCardValue(hand[6]) == getCardValue(hand[8])):
        return getCardValue(hand[4])

def getOnePairValue(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2])):
        return 7 * getCardValue(hand[0])
    elif (getCardValue(hand[2]) == getCardValue(hand[4])):
        return 7 * getCardValue(hand[2])
    elif (getCardValue(hand[4]) == getCardValue(hand[6])):
        return 7 * getCardValue(hand[4])
    elif (getCardValue(hand[6]) == getCardValue(hand[8])):
        return 7 *getCardValue(hand[6])

def getMaxValueOfOnePair(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2])):
        hand = hand [4:]
        return getCardValue(hand[4])
    elif (getCardValue(hand[2]) == getCardValue(hand[4])):
        hand = hand [0:2] + hand[4:]
        return getCardValue(hand[4])
    elif (getCardValue(hand[4]) == getCardValue(hand[6])):
        hand = hand [0:4] + hand[6:]
        return getCardValue(hand[4])
    elif (getCardValue(hand[6]) == getCardValue(hand[8])):
        hand = hand [:6]
        return getCardValue(hand[4])

def isRoyalFlush(hand):
    if  ( ( (hand[0] == 'T' or hand[2] == 'T' or hand[4] == 'T' or hand[6] == 'T' or hand[8] == 'T')
        and (hand[0] == 'J' or hand[2] == 'J' or hand[4] == 'J' or hand[6] == 'J' or hand[8] == 'J')
        and (hand[0] == 'Q' or hand[2] == 'Q' or hand[4] == 'Q' or hand[6] == 'Q' or hand[8] == 'Q')
        and (hand[0] == 'K' or hand[2] == 'K' or hand[4] == 'K' or hand[6] == 'K' or hand[8] == 'K')
        and (hand[0] == 'A' or hand[2] == 'A' or hand[4] == 'A' or hand[6] == 'A' or hand[8] == 'A'))
        and isFlush(hand)
        ):
        return True
    else: return False

def isStraightFlush(hand):
    if isStraight(hand) and isFlush(hand):
        return True
    else:
        return False

def isFourOfAKind(hand):
    if (getCardValue(hand[2]) == getCardValue(hand[4]) \
            and getCardValue(hand[4]) == getCardValue(hand[6])\
            and getCardValue(hand[6]) == getCardValue(hand[8]))\
            or (getCardValue(hand[0]) == getCardValue(hand[2]) \
            and getCardValue(hand[2]) == getCardValue(hand[4])\
            and getCardValue(hand[4]) == getCardValue(hand[6])):
        return True
    else:
        return False

def isFullHouse(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2]) and getCardValue(hand[2]) == getCardValue(hand[4]))\
            and (getCardValue(hand[6]) == getCardValue(hand[8])):
        return True
    elif (getCardValue(hand[2]) == getCardValue(hand[4]) and getCardValue(hand[4]) == getCardValue(hand[6]))\
            and (getCardValue(hand[0]) == getCardValue(hand[8])):
        return True
    elif (getCardValue(hand[4]) == getCardValue(hand[6]) and getCardValue(hand[6]) == getCardValue(hand[8]))\
            and (getCardValue(hand[0]) == getCardValue(hand[2])):
        return True
    else:
        return False

def isFlush(hand):
    if (   (hand[1] == 'S' and hand[3] == 'S' and hand[5] == 'S' and hand[7] == 'S' and  hand[9] == 'S')
        or (hand[1] == 'D' and hand[3] == 'D' and hand[5] == 'D' and hand[7] == 'D' and  hand[9] == 'D')
        or (hand[1] == 'H' and hand[3] == 'H' and hand[5] == 'H' and hand[7] == 'H' and  hand[9] == 'H')
        or (hand[1] == 'C' and hand[3] == 'C' and hand[5] == 'C' and hand[7] == 'C' and  hand[9] == 'C')
        ):
        return True
    else:
        return False

def isStraight(hand):
    counter = 0
    for h in range(0, 8, 2):
        if getCardValue(hand[h]) - getCardValue(hand[h+2]) != -1:
            counter += 1
    if counter != 0:
        return False
    else:
        return True

def isThreeOfAKind(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2]) \
            and getCardValue(hand[2]) == getCardValue(hand[4]))\
            or (getCardValue(hand[2]) == getCardValue(hand[4])\
            and getCardValue(hand[4]) == getCardValue(hand[6]))\
            or (getCardValue(hand[4]) == getCardValue(hand[6])\
            and getCardValue(hand[6]) == getCardValue(hand[8])):
        return True
    else:
        return False

def isTwoPairs(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2]))\
        and ((getCardValue(hand[2]) == getCardValue(hand[4]))\
        or  ( getCardValue(hand[4]) == getCardValue(hand[6]))\
        or  ( getCardValue(hand[6]) == getCardValue(hand[8]))):
        return True
    elif (getCardValue(hand[2]) == getCardValue(hand[4]))\
        and ((getCardValue(hand[0]) == getCardValue(hand[2]))\
        or  ( getCardValue(hand[4]) == getCardValue(hand[6]))\
        or  ( getCardValue(hand[6]) == getCardValue(hand[8]))):
        return True
    elif (getCardValue(hand[4]) == getCardValue(hand[6]))\
        and ((getCardValue(hand[0]) == getCardValue(hand[2]))\
        or  ( getCardValue(hand[2]) == getCardValue(hand[4]))\
        or  ( getCardValue(hand[6]) == getCardValue(hand[8]))):
        return True
    elif (getCardValue(hand[6]) == getCardValue(hand[8]))\
        and ((getCardValue(hand[0]) == getCardValue(hand[2]))\
        or  ( getCardValue(hand[2]) == getCardValue(hand[4]))\
        or  ( getCardValue(hand[4]) == getCardValue(hand[6]))):
        return True
    else:
        return False

def isOnePair(hand):
    if (getCardValue(hand[0]) == getCardValue(hand[2]))\
        or (getCardValue(hand[2]) == getCardValue(hand[4]))\
        or (getCardValue(hand[4]) == getCardValue(hand[6]))\
        or (getCardValue(hand[6]) == getCardValue(hand[8])):
        return True
    else:
        return False

def dividePlayerHands(listOfPlays): #ok
    player1 = []
    player2 = []
    for play in listOfPlays:
        player1.append(play[:10])
        player2.append(play[10:])
    return  [player1, player2]

def getFileFromPath(path): #ok
    hands = []
    file = open(path, 'r')
    for line in file:
        hands.append(line.rstrip().replace(' ',''))
    return hands

if __name__=="__main__":
    start = timeit.default_timer()
    royalFlushC = 'TCJCQCKCAC'
    royalFlushH = 'THJHQHKHAH'
    toSort = 'TC2C7CACKC'
    notStraight = '2C3S4H5DTD'
    straight1 = '2C3S4H5D6D'
    straight2 = '3S4H5D6D7S'
    max1 = '3S4H5D8DTS'
    max2 = '3S4H5D8DAS'
    four1 = '2S6D6S6H6C'
    four2 = '2S7D7S7H7C'
    four3 = '2C7H7S7D7C'
    three1 = '3C3D3H7C6D'
    three2 = '7C3D7H7C6D'
    three3 = '8C8D8H7C6D'
    pair1 = '2C3D6H6C9C'
    pair2 = '2C9D6H6C8C'
    twoPair1 = '2C2D6H6C8C'
    twoPair2 = '2C9D6H6C9C'

    # print isOnePair(sortCards(pair2))
    # print isTwoPairs(sortCards(twoPair1))
    # print isTwoPairs(sortCards(twoPair2))
    # print sortCards(three2)
    # print isThreOfAKind(sortCards(three2))
    # print didPlayer1Win(sortCards(three3), sortCards(three1))
    # print didPlayer1Win(pair2, pair1)
    # print didPlayer1Win(twoPair1, twoPair2)
    # print didPlayer1Win(sortCards(four2),sortCards(four3))
    # print getValueOfHand(three3)

    countWins()

    stop = timeit.default_timer()
    print("Time: ", stop - start, " s")




# def hand_rank(hand):
# 	score = zip(*sorted(((v, values[k]) for k,v in Counter(x[0] for x in hand).items()), reverse=True))
# 	score[0] = ranks.index(score[0])
# 	if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
# 	if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
# 	return score
#
# if __name__=='__main__':
#     start = timeit.default_timer()
#
#     file_url = 'https://projecteuler.net/project/resources/p054_poker.txt'
#     hands = (line.split() for line in urlopen(file_url))
#     values = {r:i for i,r in enumerate('23456789TJQKA', start=2)}
#     straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
#     ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]
#
#     print "Project Euler 54 Solution =", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands)
#
#     stop = timeit.default_timer()
#     print "Time: ", stop - start, " s"