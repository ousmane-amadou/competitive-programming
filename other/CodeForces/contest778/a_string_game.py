# SOLUTION
# To begin, we store both s and t as list of chraracters rather than a string
# and d (order of deletion) as a list of integers.
# Let t = [a,b,a,b,c,b,a], s = [a, b, b], d = [5,3,4,1,7,6,2]
#
# The solution involves emulating the deletion of
# characters in t given by the instructions described in d, and then checking
# if it is stll possible to attain the string s in t.
#
# Let c be a dictionary whose key represents a letter in t, and its value
# be a list of integers that represent the indeces in which that letter occurs
# in t (1 represents if letter exists at index). In our case we have:
#
# c = {'a':[1,0,1,0,0,0,1], 'b':[0,1,0,1,0,1,0], 'c':[0,0,0,0,1,0,0]}
# Note: c can be calculated in O(n) by just iterating through t
# and systematically editing the dictionary.
#
# Now we emulate the instrucitons given by d.
# To do this we condsider every element in d from left to right. Let this value
# be represted by D.
# t[D] would be the character to be removed.
# c[t[D]][D] would be boolean value of whether the t[D] exists at index D.
#
# Now set c[t[D]][D] = 0. We have essentially elimanted that index from play.
# The good thing about this operation is that it runs in constant [O(1)] time.
#
# What we must do now is check if s can still be attained from t.


t = list(input())
s = list(input())
d = [int(a)-1 for a in input().split()]

c = {}
lt = len(t)

# 1. Find the indeces of occurences of each character in s. O(|t|)
for i in range(lt):
    if t[i] not in c.keys():
        c[t[i]] = [0]*lt
        c[t[i]][i] = 1
    else:
        c[t[i]][i] = 1
m = 0    # Represents num of moves

# 2. Emulation O(|d|*|s|)
for D in d:
    c[t[D]][D] = 0
    q = s[:]

    ei = c[q[0]].index(1)
    q.pop(0)
    valid = True
    for a in q:
        try:
            ei = c[a].index(1, ei+1)
        except (ValueError):
            valid = False
            break
    if not valid:
        break
    else:
        m += 1

print(m)
