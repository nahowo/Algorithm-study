def solution(money):
    answer = 0
    n = len(money)
    
    for i in range(2):
        dp = [0] * (n + 1)
        if i == 0:
            dp[1] += money[0]
        
        for j in range(2, n + 1):
            dp[j] = max(dp[j - 2] + money[j - 1], dp[j - 1])
        
        if i == 0:
            answer = max(dp[n - 1], dp[n - 2])
        else:            
            answer = max(answer, max(dp[n], dp[n - 1]))
        
    return answer