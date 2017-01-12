# INCOMPLETE #
i = int(input())
j = int(input())

# For a given sequence, (n,[n+1],[n+2]....,1), adj[n] = ([n+1], count(n+1)+1),
# where count(j) is the length quantity of elements needed to reach 1.

adj = {}
max_count = 0


for k in range(i, j+1):
    if k not in adj:
        q = k
        # Generates a sequence
        while(True):
            m = q
            if m == 1:
                break
            if m % 2 == 0:
                q = int(m/2)
            else:
                q = int(3*m + 1)
            adj[m] = [q, 0]

# Recursively count the length of the sequence needed to get to n to 1
# Ex.
#    22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
#    adj[22] = [11, count(11)]
#    adj[11] = [34, count(34)]
#    .....
#    adj[2] = [2, count(2)]
#    adj[1] = [1, count(1)]
#    count(1) = 1


def count(i):
    if(i == 1):
        return 0
    else:
        adj[i][1] = count(adj[i][0]) + 1
        return adj[i][1]

for k in adj.keys():
    if (adj[k][1] == 0):
        count(k)


print(max_count)
