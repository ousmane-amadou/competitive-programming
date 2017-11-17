""" 1996 CCC Stage 1 Problem B
    Link to problem description:
        http://cemc.uwaterloo.ca/contests/computing/1996/stage1/b-prob.html

    The solution to this problem is provided in the question. All that
    is required is implementation of the divide by 11 algorithm.
"""

num_cases = int(input())
cases = []

for n in range(num_cases):
    n = int(input())
    cases.append(n)

for n in cases:
    original_num = n
    while(n >= 100):
        n = str(n)       # Convert number to string
        units = n[-1]    # Retrieve units digit
        n = n[:-1]       # Delets units digit
        n = int(n)       # Convert number to int
        n -= int(units)  # Subtract the delted digit from number

        print(n)
    if n % 11 == 0:
        print("The number " + str(original_num) + " is divisible by 11.")
    else:
        print("The number " + str(original_num) + " is not divisible by 11.")
