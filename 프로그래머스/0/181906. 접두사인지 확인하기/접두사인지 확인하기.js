function solution(my_string, is_prefix) {
    var answer = 0;
    if (my_string.slice(0, is_prefix.length) == is_prefix) {
        answer = 1;
    }
    return answer;
}