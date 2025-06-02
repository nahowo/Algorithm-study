const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    var n = Number(input[0])
    for (var i = 1; i <= n; i ++) {
        console.log("*".repeat(i))
    }
});