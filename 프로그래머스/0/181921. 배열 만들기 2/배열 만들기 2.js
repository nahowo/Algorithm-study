function solution(l, r) {
    var answer = [];
    let str = 1;
    let num = change(str);
    while (num < l) {
        str += 1;
        num = change(str);
    }
    while (l <= num && num <= r) {
        answer.push(num);
        str += 1;
        num = change(str);
    }
    if (answer.length == 0) {
        answer.push(-1);
    }
    return answer;
}

function change(str) {
    let bin = str.toString(2);
    let answer = ""
    for (let i of bin) {
        if (i == "1") {
            answer += "5";
        } else {
            answer += "0";
        }
    }
    return Number(answer);
}