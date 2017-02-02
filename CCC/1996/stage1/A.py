""" 1996 CCC Stage 1 Problem A
    Link to problem description:
        http://cemc.uwaterloo.ca/contests/computing/1996/stage1/a-prob.html


    Solution:
    Let n be any positive integer inputted.
    Let s be an integer representing the sum of proper divisors.
        1. For every integer i in [0, n/2]
        2.      if i divides evenly into n, add it to s.
        3. Test the whether s is perfect, deficient or abundant.

    Runs in O(n) time.
"""

# 1 : Retrieve number of test cases and run through code for each.
num_cases = int(input())
cases = []
for i in range(num_cases):
    n = int(input())  # A positive integer
    cases.append(n)

for n in cases:
    s = 0   # represents the sum of proper factors
    c = 1   # represents the current factor
    while c <= n/2:
        if n % c == 0:
            s += c
        c += 1
    if s == n:
        print(str(n) + " is a perfect number.")
    elif s < n:
        print(str(n) + " is a deficient number.")
    elif s > n:
        print(str(n) + " is an abundant number.")
