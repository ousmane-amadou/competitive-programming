// https://codeforces.com/problemset/problem/116/A
var n = Number(readline())

var c = 0;
var min_c = 0;

for(var i = 0; i < n; i ++) {
    var input = readline().split(' ').map(Number)
    c -= input[0]; c += input[1]
    if(c > min_c) {
        min_c = c;
    }
}

print(min_c)