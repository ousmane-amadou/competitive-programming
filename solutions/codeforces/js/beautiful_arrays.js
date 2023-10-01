var a = [];
var n=0,m=0;
for(var i = 0; i<5;i++) {
    var input = readline().trim().split(' ')
    for(var j=0;j<5;j++) {
        var b = [];
        b[j] =  Number(input[j])
        if(b[j] == 1) {
            n = i; m=j;
        }
    } 
}
sol = Math.abs(2-n) + Math.abs(2-m)
print(sol)
