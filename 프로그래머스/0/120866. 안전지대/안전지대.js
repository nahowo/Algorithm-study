function solution(board) {
    var answer = 0;
    let n = board.length;
    for (let i = 0; i < n; i ++) {
        for (let j = 0; j < n; j ++) {
            if (board[i][j] == 0) {
                answer += checkDangerZone(board, i, j, n);
            }
        }
    }
    return answer;
}

function checkDangerZone(board, i, j, n) {
    const direction = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]];
    for (let [di, dj] of direction) {
        let ni = i + di;
        let nj = j + dj;
        if (0 <= ni && ni < n && 0 <= nj && nj < n) {
            if (board[ni][nj] == 1) {
                return 0;
            }
        }
    }
    return 1;
}