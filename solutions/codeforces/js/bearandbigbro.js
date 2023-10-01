/*
 * https://codeforces.com/problemset/problem/791/A 
*/
var ages = readline().split(' ').map(Number)

var num_years = 0;

while(true) {
    num_years++;
    if (ages[0] >= ages[1]) {
        break
    } else{
        ages[0]*=2
    }
}
print(num_years)
