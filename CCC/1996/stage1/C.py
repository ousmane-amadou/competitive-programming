""" 1996 CCC Stage 1 Problem C
    Link to problem description:
        http://cemc.uwaterloo.ca/contests/computing/1996/stage1/c-prob.html

    0*2^0 + 2^1 + 2^2 ... + 2^n
"""

num_cases = int(input())
pairs = []
for case in range(num_cases):
    i, j = map(int, input().split())
    pairs.append([i, j])

for pair in pairs:
    n, k = pair
