function solution(number) {
    var answer = 0;
    var numbers = number.split("");
    var sum = 0;
    for (var i = 0; i < numbers.length; i ++) {
        sum += parseInt(numbers[i]);
    }
    answer = sum % 9;
    return answer;
}