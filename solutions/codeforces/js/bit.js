var x = Number(readline())
var sol = 0;
for(var i = 0; i < x; i++){
    var input = readline()
    if (input.substring(0, 2) == "++" || input.substring(1, 3) == "++") {
        sol++;
    }
    if (input.substring(0, 2) == "--" || input.substring(1, 3) == "--") {
        sol--;
    }
}
print(sol)