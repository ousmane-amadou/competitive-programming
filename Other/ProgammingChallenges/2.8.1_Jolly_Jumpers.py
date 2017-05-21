# SOLN:
#   Keep a
#
#

while True:
    stdin = input()
    if stdin == ' ':
        break

    stdin = list(map(int, stdin.split()))
    m = max(stdin) - 1
    jld = {}                                # Jolly Dictionary = Holds
    s = 0
    for i in range(len(stdin) - 1):
        diff = stdin[i+1] - stdin[i]
        if diff < 0:
            diff = -1*diff

        if not diff > m:
            if diff not in jla.keys():
                s += 1
                jla[diff] = 1

    if s == max(stdin) - 1:
        print("Jolly")
    else:
        print("Not Jolly")
