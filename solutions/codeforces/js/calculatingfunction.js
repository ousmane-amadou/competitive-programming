// https://codeforces.com/problemset/problem/486/A

function f(n) {
    if (n==1){
        return -1
    } else {
        var sol = Math.pow(-1, n) * n + f(n-1)
        return sol
    }
}

n = Number(readline())

print(f(n))