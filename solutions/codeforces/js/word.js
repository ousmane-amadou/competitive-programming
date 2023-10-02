// https://codeforces.com/problemset/problem/59/A
var word = readline()

var num_upper = 0
var num_lower = 0

for(var i = 0; i < word.length; i++) {
    if(word.charAt(i).toUpperCase() == word.charAt(i)) {
        num_upper++
    } else {
        num_lower++
    }
}
if(num_upper > num_lower) {
    print(word.toUpperCase())
} else {
    print(word.toLowerCase())
}