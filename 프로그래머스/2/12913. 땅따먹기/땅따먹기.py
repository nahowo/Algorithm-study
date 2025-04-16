from copy import deepcopy
def solution(land):
    answer = 0
    n = len(land)
    dp = deepcopy(land)
    
    for i in range(1, n):
        choice = deepcopy(dp[i - 1])
        for j in range(4):
            choice[j] = 0
            dp[i][j] += max(choice)
            choice[j] = dp[i - 1][j]
    answer = max(dp[n - 1])

    return answer