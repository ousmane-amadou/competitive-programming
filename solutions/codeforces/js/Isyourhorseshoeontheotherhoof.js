var h = readline().split(' ')

var unique = 4; // Assume that you have all unique input
var seen = []
for(var i = 0; i < 4; i++) {
   if(seen.includes(h[i])) {
        unique--;
   } else {
        seen.push(h[i]);
   }
}
print(4-unique) // Print out number needed to have all unique input