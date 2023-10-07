var x = readline()
var y = readline()

var sol = ""
for(var i = 0; i < x.length; i++) {
    if(x.charAt(i) != y.charAt(i)) {
        sol += "1"
    } else {
        sol += "0"
    }
}
print(sol)