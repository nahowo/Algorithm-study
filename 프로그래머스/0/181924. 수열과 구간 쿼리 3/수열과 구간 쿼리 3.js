function solution(arr, queries) {
    var answer = JSON.parse(JSON.stringify(arr))
    var n = queries.length
    
    for (var k = 0; k < n; k ++ ) {
        var i = queries[k][0]
        var j = queries[k][1]
        var tmp = answer[i]
        answer[i] = answer[j]
        answer[j] = tmp
    }
    
    return answer;
}