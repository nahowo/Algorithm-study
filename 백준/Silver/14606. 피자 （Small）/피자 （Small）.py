import sys
input = sys.stdin.readline

def recursion(i, j):
    if i == 0 or j == 0:
        return 0
    if i == 1 and j == 1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    if i % 2 == 0:
        i1 = i2 = i // 2
    else:
        i1 = i // 2
        i2 = i // 2 + 1

    if j % 2 == 0:
        j1 = j2 = j // 2
    else:
        j1 = j // 2
        j2 = j // 2 + 1
        
    ret = i * j + recursion(i1, i2) + recursion(j1, j2)
    dp[i][j] = ret
    return ret

def solution():
    global dp
    n = int(input())
    dp = [[-1] * 11 for _ in range(11)]
    if n % 2 == 0:
        return recursion(n // 2, n // 2)
    else:
        return recursion(n // 2, n // 2 + 1)

print(solution())