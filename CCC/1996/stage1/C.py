""" 1996 CCC Stage 1 Problem C
    Link to problem description:
        http://cemc.uwaterloo.ca/contests/computing/1996/stage1/c-prob.html

    Solution:
    1. Let n be the length of the bit string.
    2. Let k bt the number of ones in the bit string.
    3. Find the initial bitstring with k ones followed by n-k zeroes.
    4. Left shift all the bits with the exception of the first bit.
    5.

    Consider n=6, k=3.
    1 11000

    1 01100
    1 00110
    1 00011

    11 0110
    11 0011

    111 000
"""

nc = int(input())           # Read in number of cases
cases = [[0, 0]*nc]         # A queue to hold the cases we want to deal with

for i in range(nc):
    cases[i][0], cases[i][1] = map(int, input().split())

for case in cases:
    ibp = 0
    n, k = case
    for i in range(k):
        ibp += 2**(n-i)

    print(ibp)
