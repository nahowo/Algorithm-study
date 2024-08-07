import sys
input = sys.stdin.readline

def solution():
    s1 = ' ' + input().rstrip()
    s2 = ' ' + input().rstrip()
    l1 = len(s1)
    l2 = len(s2)

    dp = [[''] * (l1) for _ in range(l2)]
    for i in range(1, l2):
        for j in range(1, l1):
            if s2[i] == s1[j]:
                dp[i][j] = dp[i - 1][j - 1] + s1[j]
            else:
                if len(dp[i - 1][j]) > len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 1]
    print(len(dp[l2 - 1][l1 - 1]))
    print(dp[l2 - 1][l1 - 1])
    return

solution()