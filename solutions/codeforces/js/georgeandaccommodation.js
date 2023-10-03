// https://codeforces.com/problemset/problem/467/A

var r = readline()

var free = 0;
for(var i = 0; i < r; i++) {
    var ip = readline().split(' ').map(Number)
    if(ip[1] -ip[0] >= 2){
        free++
    }
}
print(free)