// https://codeforces.com/problemset/problem/344/A

var n = Number(readline())
var g = 1;

var m1 = readline()
for(var i = 1; i<n; i++) {
    var m2 = readline()
    if(m1 != m2) {
        g+=1
    }
    m1 = m2;
}
print(g)