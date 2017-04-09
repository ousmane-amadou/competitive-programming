#  10 denotes a Straight Flush
#   9 denotes a four of a kind
#   8 denotes a fullhouse


def vald(a):
    vald = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
            '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return vald[a]


def isSF(h):
    return h[0] == h[1] == h[2] == h[3] == h[4] == h[5]


def isFK(h):
    bf1 = h[0] == h[1] == h[2] == h[3] == h[4]
    bf2 = h[1] == h[2] == h[3] == h[4] == h[5]
    return bf1 or bf2


def isFH(h):
    sorted(vald, key=vald)
    bf1 = h[0][0] == h[1][0] == h[2][0] == h[3][0] == h[4][0]
    bf2 = h[1][0] == h[2][0] == h[3][0] == h[4][0] == h[5][0]
    return bf1 or bf2


while True:
    cards = input().split(' ')
    if len(cards) == 0:
        break

    p1h = [cards[0], cards[1], cards[2], cards[3], cards[4]]
    p2h = [cards[5], cards[6], cards[7], cards[8], cards[9]]

    p1r = [-1, -1]
    p2r = [-1, -1]

    i = 10
    win = [0, 0]
    while (p1r == [-1, -1]) or (p2r == [-1, -1]):
        if i == 10:
            if ifSF(p1h):
                p1r = [10, cards[0][0]]
                win[0] = 1
            if ifSF(p2h):
                p1r = [10, cards[0][0]]
                win[1] = 1
        elif i == 9:
            if isFK(p1h):
                p1r = [10, cards[3][0]]
                win[0] = 1
            if isFK(p2h):
                p1r = [10, cards[3][0]]
                win[1] = 1
        elif i == 8:
            if ifSF(p1h):
                p1r = [10, cards[3][0]]
                win[0] = 1
            if ifSF(p2h):
                p1r = [10, cards[3][0]]
                win[1] = 1
