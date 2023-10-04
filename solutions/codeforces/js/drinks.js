// https://codeforces.com/problemset/problem/200/B

var n = readline()
var p = readline().split(' ').map(Number)
var sol = 0.0

for(var i = 0; i < n; i++) {
    sol += p[i]
}

sol /= n
print(sol)
