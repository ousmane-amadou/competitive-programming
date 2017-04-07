# Solution:
#   Let c be an array of length n. where for all i <= n. c[i] represents the
#   total amount of money spent by a student i.
#   Let ec represent the "equalized cost", that is the amount of money each
#   student should pitch.
#   1. First we will calculate the ec.
#   2. Sort c from least to greatest.
#   The optimal way to move money around, is by taking the cost of comeone who
#   spent the most and adding it to the cost of someone who spent the least.
#   3. Start at both ends of c. (c[i] and c[n-(i+1)]) Compare these values
#   with ec, and add subtract accordingly

# Search up how to do continual input until input equals 0
# Search up how to format string to money in python

# Works for given test cases.... may want to try for others... algorithm
# may be broken somewhere..
output = []
while True:
    n = int(input())      # number of students
    if n == 0:
        break

    c = []                # cost array
    ec = 0                # equalized cost per student
    for i in range(n):
        s = float(input())
        ec += s
        c.append(s)
    ec /= n                # final value ofequalized cost

    c.sort()
    me = 0                 # money exchanged.
    lo = 0
    hi = n - 1

    while(lo < hi):
        lo_diff = ec - c[lo]
        hi_diff = c[hi] - ec

        if lo_diff == hi_diff:
            lo += 1
            hi -= 1
            me += hi_diff
        elif lo_diff < hi_diff:
            lo += 1
            c[hi] -= lo_diff
            me += lo_diff
        else:
            c[lo] += hi_diff
            hi -= 1
            me += hi_diff

    output.append(me)

for o in output:
    print o
