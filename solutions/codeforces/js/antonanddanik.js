// https://codeforces.com/problemset/problem/734/A

var n = Number(readline())
var s = readline()

var agw=0; var dgw=0;
for(var i = 0; i < n; i++) {
    if(s.charAt(i) == 'A') {
        agw++;
    } else {
        dgw++;
    }
}

if(agw == dgw) {
    print('Friendship')
} else if(agw > dgw) {
    print('Anton')
} else {
    print('Danik')
}