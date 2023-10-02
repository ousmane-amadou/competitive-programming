var s = readline()
var t = readline()

var sol ="YES"
for (var i =0; i <s.length; i++) {
    if(s[i] != t[t.length-1-i]) {
        sol = "NO"
    }
}
print(sol)