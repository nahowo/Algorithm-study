def solution(n, results):
    answer = 0
    match = [[set(), set()] for _ in range(n + 1)] # win, lose
    for a, b in results:
        match[a][0].add(b)
        match[b][1].add(a)
    
    for i in range(1, n + 1):
        for j in match[i][1]: # j > i
            match[j][0].update(match[i][0])
        for j in match[i][0]: # i > j
            match[j][1].update(match[i][1])

    for i in range(1, n + 1):
        if len(match[i][0]) + len(match[i][1]) == n - 1:
            answer += 1
    
    return answer