function solution(my_string, overwrite_string, s) {
    var answer = '';
    for (i = 0; i < s; i ++) {
        answer += my_string[i]
    }
    for (i = 0; i < overwrite_string.length; i ++) {
        answer += overwrite_string[i]
    }
    for (i=s+overwrite_string.length; i < my_string.length; i ++) {
        answer += my_string[i]
    }
    return answer;
}