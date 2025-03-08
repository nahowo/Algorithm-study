def solution(info, n, m):
    INF = 10 ** 3
    l = len(info)
    dp = [[INF] * (m + 1) for _ in range(l + 1)]
    for j in range(m):
        dp[0][j] = 0
    for i in range(1, l + 1):
        for j in range(m + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + info[i - 1][0])
            if j + info[i - 1][1] < m:
                dp[i][j + info[i - 1][1]] = dp[i - 1][j]
        
    if min(dp[l]) >= n:
        return -1
    return min(dp[l])