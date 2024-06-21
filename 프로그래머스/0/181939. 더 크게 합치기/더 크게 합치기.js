function solution(a, b) {
    var answer = 0;
    var tmp1 = Number(String(a) + String(b));
    var tmp2 = Number(String(b) + String(a));
    answer = Math.max(tmp1, tmp2)
    return answer;
}