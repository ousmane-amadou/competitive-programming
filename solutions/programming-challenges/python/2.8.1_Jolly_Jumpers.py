# Solved
# Type: Ad-hoc
# Skill: Beginner
# Concepts Involved : Arrays
while True:
    n = map(int, raw_input().split(" "))
    n = n[1:]

    c = 0                  # The number of unique jumps that have occured

    jump = [False]*3000    # jump[i] is a bool value representing whether
                           # a jump of i has occured in the sequence

    jump[0] = True         # We'd like to ignore jumps of 0

    for i in range(len(n)-1):
        diff = abs(n[i] - n[i+1])
        if jump[diff] == False and diff <= len(n)-1:
            jump[diff] = True
            c += 1

    if c == len(n)-1:
        print "Jolly"
    else:
        print "Not Jolly"
