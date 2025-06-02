function solution(numLog) {
    var answer = '';
    var n = numLog.length
    
    for (var i = 1; i < n; i ++) {
        var diff = numLog[i] - numLog[i - 1];
        answer += command(diff)
    }
    
    return answer;
}

function command(diff) {
    if (diff == 1) {
        return "w"
    } else if (diff == -1) {
        return "s"
    } else if (diff == 10) {
        return "d"
    } else if (diff == -10) {
        return "a"
    } 
}