function solution(money) {
    var coffeeCount = Math.floor(money / 5500)
    var left = money % 5500
    var answer = [coffeeCount, left];
    return answer;
}