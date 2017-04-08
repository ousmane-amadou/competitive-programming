nums = {0: [1, 1, 1, 0, 1, 1, 1], 1: [0, 0, 1, 0, 0, 0, 1],
        2: [1, 0, 1, 1, 1, 1, 0], 3: [1, 0, 1, 1, 0, 1, 1],
        4: [0, 1, 1, 1, 0, 0, 1], 5: [1, 1, 0, 1, 0, 1, 1],
        6: [1, 1, 0, 1, 1, 1, 1], 7: [1, 0, 1, 0, 0, 1, 0],
        8: [1, 1, 1, 1, 1, 1, 1], 9: [1, 1, 1, 1, 0, 1, 1]}

while True:
    s, n = input().split()
    s = int(s)

    if s == 0 and n == "0":
        break
    output = ""
    for i in n:
        for j in range(1, (s+2) + 1):
            if j == 1:  # Deals with top comment
                output += " " + nums[i][0]*s + " "
            elif j > 1 and j < 1 + s:
                #
            else:
