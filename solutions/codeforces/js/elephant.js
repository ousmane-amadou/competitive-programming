// https://codeforces.com/problemset/problem/617/A
var x = Number(readline())

var sol = 0

while(x>=1) {
    if(x>=5) {
        sol +=1
        x-=5;
    } else if(x == 4) {
        sol += 1
        x-=4
    } else if(x == 3) {
        sol += 1
        x-=3
    }else if(x == 2) {
        sol += 1
        x-=2
    } else {
        sol+=1
        x -= 1 
    }
}

print(sol)