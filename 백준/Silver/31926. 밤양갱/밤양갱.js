route = "dev/stdin";

const fs = require("fs");
const input = fs.readFileSync(route).toString();

function inputProcess() {
    n = Number(input);
}

function solution() {
    let time = 8;
    let cnt = 1;
    while (1) {
        if (cnt > n) {
            return time + 1;
        } else if (cnt == n) {
            return time + 2;
        } else {
            cnt *= 2;
            time += 1;
        }
    }
}

inputProcess();
const answer = solution();
console.log(answer);