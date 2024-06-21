const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    answer = "";
    for (i = 0; i < str.length; i++) {
        tmp = str[i].charCodeAt();
        if (65 <= tmp && tmp <= 90) {
            answer += String.fromCharCode(tmp+32);
        } else {
            answer += String.fromCharCode(tmp-32);
        }
    }
    console.log(answer)
});