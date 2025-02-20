def solution(info, n, m):
    maxSize = 10 ** 6
    l = len(info)
    dp = [[maxSize] * (m) for _ in range(l + 1)]
    dp[0][0] = 0
    
    for i in range(1, l + 1):
        a, b = info[i - 1]
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)
            if j + b < m:
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])
                
        answer = min(dp[l])
        if answer >= n:
            answer = -1
    return answer