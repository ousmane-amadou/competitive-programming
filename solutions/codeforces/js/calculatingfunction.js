// https://codeforces.com/problemset/problem/486/A

function f2(n) {
    var sol = 0;
    for(var i = 1; i <= n; i++) {
        if (i%2 == 1) {
            sol -= i
        } else {
            sol += i
        }
    }
    return sol;
}
function f(n) {
    if (n==1){
        return -1
    } else {
        var sol = Math.pow(-1, n) * n + f(n-1)
        return sol
    }
}

n = Number(readline())

print(f2(n))