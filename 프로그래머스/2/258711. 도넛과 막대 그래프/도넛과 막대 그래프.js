function solution(edges) {
    var answer = [0, 0, 0, 0];
    let io = new Map(); // [in, out]
    for (let [a, b] of edges) {
        if (io.has(a) == false) {
            io.set(a, [0, 1]);
        } else {
            io.get(a)[1] += 1;
        }
        if (io.has(b) == false) {
            io.set(b, [1, 0]);
        } else {
            io.get(b)[0] += 1;
        }
    }
    
    let totalCount;
    for (let [number, degree] of io) {
        let [i, o] = degree;
        if ((i == 2 || i == 3) && o == 2) { // 8자
            answer[3] += 1;
        } 
        else if (o == 0) { // 막대
            answer[2] += 1;
        }
        else if (o >= 2 && i == 0) { // 임의의 정점
            answer[0] = number;
            totalCount = o;
        }
    }
    answer[1] = totalCount - answer[2] - answer[3];
    
    return answer;
}