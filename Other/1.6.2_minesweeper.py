i, j = map(int, input().split())
board = []

for a in range(i):
    line = list(input())
    for ch in line:
        board.append(ch)

mirror = []
for p in range(len(board)):
    star_count = 0

    # Search up boolean formulas...
    left = (p % j) == 0
    right = ((p + j) % 4) == 0
    top = p < j
    bottom = p >= (i-1)*j

    star_count = left*
