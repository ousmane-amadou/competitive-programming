var s = readline()

var o = 0; var t = 0
var sol = "NO"

for(var i = 0; i<s.length; i++) {
    if(s.charAt(i)=='0') {
        o++; t=0;
    } else {
        t++; o=0;
    }
    if(o == 7 || t ==7) {
        sol="YES"
    }
}

print(sol)