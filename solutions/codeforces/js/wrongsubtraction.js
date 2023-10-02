// https://codeforces.com/problemset/problem/977/A

var input = readline().split(' ').map(Number)
n = input[0]; k = input[1]

for(var i = 0; i <k; i++){
    if (n%10 == 0) {
        n/=10
    } else{
        n--;
    }
}

print(n)