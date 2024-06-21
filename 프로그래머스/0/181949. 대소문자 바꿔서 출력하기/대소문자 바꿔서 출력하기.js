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
        tmp = str[i];
        if (tmp === tmp.toLowerCase()) { // 소문자인 경우
            answer += tmp.toUpperCase();
        } else {
            answer += tmp.toLowerCase();
        }
    }
    console.log(answer)
});