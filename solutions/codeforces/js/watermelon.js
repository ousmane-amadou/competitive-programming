function sol(weight) {
    if ((weight <=2) || (weight % 2 == 1)) {
        return "NO"
    } else {
        return "YES"
    } 
}

var w = Number(readline())
print(sol(w))

module.exports = {
    sol
}