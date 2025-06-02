function solution(my_string, n) {
    var answer = '';
    var len = my_string.length
    
    for (var i = 0; i < len; i ++) {
        answer += my_string[i].repeat(n)
    }
    
    return answer;
}