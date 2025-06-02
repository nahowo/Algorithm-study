function solution(num_list) {
    var n = Math.floor(num_list.length / 2)
    
    for (var i = 0; i < n; i ++) {
        var j = num_list.length - i - 1
        var tmp = num_list[j]
        num_list[j] = num_list[i]
        num_list[i] = tmp
    }
    var answer = JSON.parse(JSON.stringify(num_list));
    return answer;
}