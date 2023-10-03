// https://codeforces.com/problemset/status?my=on
var y = readline(); 

function is_distinct(year) {
    var s = String(year)
    var in_s = []
    for(var i = 0; i <s.length; i++){
        if(in_s.includes(s.charAt(i))){
            return false;
        } else {
            in_s.push(s.charAt(i))
        }
    }
    return true;
}

do {
    y++;
}
while(!is_distinct(y)) 

print(y++)