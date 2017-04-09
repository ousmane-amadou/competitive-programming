#  10 denotes a Straight Flush
#   9 denotes a four of a kind
#   8 denotes a fullhouse

VALS = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def vald(a):
    return VALS[a]


def isSF(h):
    r = [-1, -1]
    if h[0] == h[1] == h[2] == h[3] == h[4]:
        r = [10, h[4][0]]
    return r


def isFK(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][0] == h[1][0] == h[2][0] == h[3][0]:
        r = [9, h[3][0]]
    elif [1][0] == h[2][0] == h[3][0] == h[4][0]:
        r = [9, h[3][0]]
    return r


def isFH(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if (h[0][0] == h[1][0] == h[2][0]) and (h[3][0] == h[4][0]):
        r = [8, h[2][0]]
    elif (h[1][0] == h[2][0]) and (h[3][0] == h[4][0] == h[5][0]):
        r = [8, h[3][0]]
    return r


def isFL(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][1] == h[1][1] == h[2][1] == h[3][1] == h[4][1]:
        r = [7, h[4][1]]
    return r


def isST(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    bf1 = VALS[h[1][0]] == (VALS[h[0][0]] + 1)
    bf2 = VALS[h[2][0]] == (VALS[h[1][0]] + 1)
    bf3 = VALS[h[3][0]] == (VALS[h[2][0]] + 1)
    bf4 = VALS[h[4][0]] == (VALS[h[3][0]] + 1)
    if bf1 and bf2 and bf3 and bf4:
        r = [6, h[4][0]]

    return [-1, -1]


def isTOK(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    bf1 = (h[0][0] == h[1][0] == h[2][0])
    bf2 = (h[1][0] == h[2][0] == h[3][0])
    bf3 = (h[2][0] == h[3][0] == h[4][0])
    if bf1 or bf2 or bf3:
        r = [5, h[2][0]]


def is2P(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][0] == h[1][0] and h[1][0] == h[2][0]:
        r = [4, h[1][0]]
    if h[2][0] == h[3][0] and h[3][0] == h[4][0]:
        r = [4, max(r[1], h[3][0])]
    return r


def isP(h):
    sorted(vald, key=vald)
    r = [-1, -1]
    if h[0][0] == h[1][0] or h[1][0] == h[2][0]:
        r = [3, h[1][0]]
    elif h[2][0] == h[3][0] or h[3][0] == h[4][0]:
        r = [3, h[3][0]]
    return r


def isHC(h):
    sorted(vald, key=vald)
    return [2, h[4][0]]

while True:
    cards = input().split(' ')
    if len(cards) == 0:
        break

    p1h = [cards[0], cards[1], cards[2], cards[3], cards[4]]
    p2h = [cards[5], cards[6], cards[7], cards[8], cards[9]]

    p1r = [-1, -1]
    p2r = [-1, -1]

    i = 10
    winner = -1
    while winner == -1 or i < 2:
        if i == 2:
            p1r = isHC(p1h)
            p2r = isHC(p2h)
        elif i == 3:
            p1r = isP(p1h)
            p2r = isP(p2h)
        elif i == 4:
            p1r = is2P(p1h)
            p2r = is2P(p2h)
        elif i == 5:
            p1r = isTOK(p1h)
            p2r = isTOK(p2h)
        elif i == 6:
            p1r = isST(p1h)
            p2r = isST(p2h)
        elif i == 7:
            p1r = isFL(p1h)
            p2r = isFL(p2h)
        elif i == 8:
            p1r = isFH(p1h)
            p2r = isFH(p2h)
        elif i == 9:
            p1r = isFK(p1h)
            p2r = isFK(p2h)
        elif i == 10:
            p1r = isSF(p1h)
            p2r = isSF(p2h)
        i -= 1
        # Handle Aftermath of looking at hands
        if p1r[0] == -1 and p2r[0] == -1:
            pass
        elif p1r[0] == -1:
            winner = 2
            break
        elif p2r[0] == -1:
            winner = 1
            break
        else:
            if p1r[1] == p2r[1]:
                pass
            elif p1r[1] > p2r[1]:
                winner = 1
            else:
                winner = 2
    if winner == -1:
        print 'Tie.'
    elif winner == 1:
        print 'Black Wins.'
    else:
        print 'White Wins.'
