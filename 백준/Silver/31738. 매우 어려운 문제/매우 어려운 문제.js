route = "dev/stdin";

const fs = require("fs");
const input = fs.readFileSync(route).toString();

function inputProcess() {
    let tmp = input.split(" ");
    n = Number(tmp[0]);
    m = Number(tmp[1]);
}

function solution() {
    if (n >= m) {
        return 0;
    }
    let answer = 1;
    for (let i = n; i > 0; i --) {
        answer *= (i % m);
        answer %= m;
    }
    return answer;
}

inputProcess()
const answer = solution()
console.log(answer)