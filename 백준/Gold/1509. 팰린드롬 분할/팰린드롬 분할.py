import sys
input = sys.stdin.readline
MAX_SIZE = 2500

def solution():
    s = input().rstrip()
    n = len(s)
    palindrome = [[0] * (n) for _ in range(n)]
    
    for i in range(n):
        palindrome[i][i] = 1
    
    for i in range(1, n):
        if s[i - 1] == s[i]:
            palindrome[i - 1][i] = 1

    for j in range(2, n): # 종료
        for i in range(j - 1): # 시작
            if palindrome[i + 1][j - 1] and s[i] == s[j]:
                palindrome[i][j] = 1

    dp = [MAX_SIZE] * (n + 1)
    dp[0] = 0
    for j in range(n + 1):
        for i in range(1, j + 1):
            if palindrome[i - 1][j - 1]:
                dp[j] = min(dp[j], dp[i - 1] + 1)
    return dp[n]

print(solution())