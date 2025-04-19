def solution(n):
    direction = [(1, 0), (0, 1), (-1, -1)]
    answer = [[0] * (i + 1) for i in range(n)]
    i, j = -1, 0
    
    cnt = n
    number = 1
    for k in range(n):
        di, dj = direction[k % 3]
        for _ in range(cnt):
            i, j = i + di, j + dj
            answer[i][j] = number
            number += 1
        cnt -= 1
    
    return sum(answer, [])