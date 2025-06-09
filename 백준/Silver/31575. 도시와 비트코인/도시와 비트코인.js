route = "dev/stdin";

const fs = require("fs");
const input = fs.readFileSync(route).toString();
const direction = [[0, 1], [1, 0]];

function inputProcess() {
    let tmp = input.split("\n");
    let nm = tmp[0].split(" ");
    n = Number(nm[0]);
    m = Number(nm[1]);
    board = [];
    for (let i = 1; i <= m; i ++) {
        board.push(tmp[i].toString().trim().split(" "));
    }
}

function solution() {
    let visited = Array.from(Array(m), () => Array(n).fill(false));
    visited[0][0] = true;
    q = [[0, 0]];
    while (q.length > 0) {
        let cur = q.shift();
        let x = cur[0];
        let y = cur[1];
        for (let i = 0; i < direction.length; i ++) {
            let nx = x + direction[i][0];
            let ny = y + direction[i][1];
            if ((0 <= nx && nx < m) && (0 <= ny && ny < n)) {
                if ((visited[nx][ny] == false) && board[nx][ny] == '1') {
                    visited[nx][ny] = true;
                    q.push([nx, ny]);
                }
            }
        }
    }
    if (visited[m - 1][n - 1] == true) {
        return "Yes";
    }
    return "No";
}

inputProcess();
const answer = solution();
console.log(answer);