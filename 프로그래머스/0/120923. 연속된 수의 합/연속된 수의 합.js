function solution(num, total) {
    var answer = [];
    let start;
    if (num % 2 == 0) {
        start = Math.floor(total / num) - Math.floor((num - 2) / 2);
    } else {
        start = Math.floor(total / num) - Math.floor((num - 1) / 2);
    }
    
    for (let i = start; i < start + num; i ++) {
        answer.push(i);
    }
    return answer;
}