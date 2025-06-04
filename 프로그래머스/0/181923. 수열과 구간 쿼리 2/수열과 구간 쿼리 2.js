MAX_SIZE = 10 ** 6 + 1

function solution(arr, queries) {
    var n = queries.length
    var answer = Array.from({length: n}, (v, i) => 0);
    
    for (var i = 0; i < n; i ++) {
        answer[i] = search(arr, queries[i][0], queries[i][1], queries[i][2])
    }
    
    return answer;
}

function search(arr, s, e, k) {
    var answer = MAX_SIZE
    for (var i = s; i <= e; i ++) {
        if (arr[i] > k) {
            answer = Math.min(answer, arr[i])
        }
    }
    if (answer < MAX_SIZE) {
        return answer
    }
    return -1
}