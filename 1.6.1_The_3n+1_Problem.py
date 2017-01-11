## INCOMPLETE ##
i = int(input())
j = int(input())

# For a given sequence, (n,[n+1],[n+2]....,1), adj[n] = ([n+1], count(n+1)+1), where
# count(j) is the length quantity of elements needed to reach 1.

adj = {}

for k in range(i,j+1):
    if k not in adj:
        m=k
        while(True):
            if m==1:
                break
            if m%2==0:
                m = int(m/2)
            else:
                m = int(3*m +1)
            adj[k] = [m,0]
            print(m),
        print()

max_count = 0
def count(i):
    if(i == 0):
        return 1
    else:
        adj[i] = [adj[i][0], count(adj[adj[i]][0])]
        max_count = max(max_count, count(adj[adj[i]][0]))
