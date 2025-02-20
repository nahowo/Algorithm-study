def solution(players, m, k):
    answer = 0
    n = len(players)
    build = [0] * n
    
    a = [0] * n
    for i in range(n):
        need = max(players[i] // m - build[i], 0)
        a[i] = need
        answer += need
        for j in range(k):
            if i + j < 24:
                build[i + j] += need

    return answer