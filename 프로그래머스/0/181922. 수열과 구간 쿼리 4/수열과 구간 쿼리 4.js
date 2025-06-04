function solution(arr, queries) {
    var n = queries.length
    
    for (var i = 0; i < n; i ++) {
        arr = add(arr, queries[i][0], queries[i][1], queries[i][2])
    }
    return arr
}

function add(arr, s, e, k) {
    for (var i = s; i <= e; i ++) {
        if (i % k == 0) {
            arr[i] += 1
        }
    }
    return arr
}