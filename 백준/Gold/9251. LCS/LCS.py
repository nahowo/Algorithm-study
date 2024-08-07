import sys
input = sys.stdin.readline

def solution():
    s1 = ' ' + input().rstrip()
    s2 = ' ' + input().rstrip()
    l1 = len(s1)
    l2 = len(s2)

    dp = [[0] * (l1) for _ in range(l2)]
    for i in range(1, l2):
        for j in range(1, l1):
            if s2[i] == s1[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[l2 - 1][l1 - 1]

print(solution())