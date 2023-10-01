/* 
 * Link to problem: https://codeforces.com/problemset/problem/266/A
 */
var stone_length = Number(readline())
var stones = readline()

function deleteCharAt(str, i) {
    return str.substring(0, i+1) + str.slice(i+2)
}

var sol = 0;


for(var i = 0; i < stone_length-1; i++) {
    if(stones.length == 1) {
        break
    }
    if(stones.charAt(i) == stones.charAt(i+1)) {
        stones = deleteCharAt(stones, i)
        i--; sol++;
    }   
}

print(sol);


