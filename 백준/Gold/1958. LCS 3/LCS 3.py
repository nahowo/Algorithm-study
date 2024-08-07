import sys
input = sys.stdin.readline

def lcsLength(s1, s2, s3):
    l1 = len(s1)
    l2 = len(s2)
    l3 = len(s3)

    dp = [[[0] * (l1) for _ in range(l2)] for _ in range(l3)]
    for i in range(1, l3):
        for j in range(1, l2):
            for k in range(1, l1):
                if s3[i] == s2[j] == s1[k]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])
    
    return dp[l3 - 1][l2 - 1][l1 - 1]

def solution():
    a = ' ' + input().rstrip()
    b = ' ' + input().rstrip()
    c = ' ' + input().rstrip()
    return lcsLength(a, b, c)

print(solution())