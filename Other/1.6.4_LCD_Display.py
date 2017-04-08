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
        for j in range(0, (2s+3)):
            if j == 0:  # Deals with quad 0
                if nums[i][0]:
                    output += " " + "-"*s + " "
                else:
                    output += " " + " "*s + " "
            elif j > 0 and j < 1 + s:       # Deals with 1st and 2nd quads
                if num[i][1]:
                    output += "|"
                else:
                    output += " "
                output = " "*s
                if num[i][2]:
                    output += "|"
                else:
                    output += " "
            elif j == 1 + s:                # Deals with the third quad
                if nums[i][3]:
                    output += " " + "-"*s + " "
                else:
                    output += " " + " "*s + " "
            elif j > 1 + s and j < 2s + 2:  # Deals with the 4th and 6th quads
                if num[i][4]:
                    output += "|"
                else:
                    output += " "
                output = " "*s
                if num[i][6]:
                    output += "|"
                else:
                    output += " "
            else:                           # Deals with the 5th
                if nums[i][5]:
                    output += " " + "-"*s + " "
                else:
                    output += " " + " "*s + " "

print(output)
