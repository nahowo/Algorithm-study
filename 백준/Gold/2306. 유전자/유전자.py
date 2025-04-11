import sys
input = sys.stdin.readline

def solution():
    dna = input().rstrip()
    n = len(dna)
    dp = [[0] * n for _ in range(n)]

    for l in range(1, n):
        for i in range(n - l):
            j = i + l
            if (dna[i] == 'a' and dna[j] == 't') or (dna[i] == 'g' and dna[j] == 'c'):
                dp[i][j] = dp[i + 1][j - 1] + 2
            for k in range(i, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k + 1][j])

    return dp[0][n - 1]
    
print(solution())