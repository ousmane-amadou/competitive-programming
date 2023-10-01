
var numCases = Number(readline())
var possibilites = ["1 1 1", "1 0 1", "0 1 1", "1 1 0"]
var sol = 0;

for (var i =0; i < numCases; i++) {
    var cse = readline()
    for (var j = 0; j < possibilites.length; j++) {
        if (possibilites[j] == cse.trim()) {
            sol++;
            break;
        }
    }
}

print(sol)

