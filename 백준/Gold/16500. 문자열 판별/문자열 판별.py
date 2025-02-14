import sys
input = sys.stdin.readline

def solution():
    s = input().rstrip()
    l = len(s)
    n = int(input())
    arr = set([input().rstrip() for _ in range(n)])
    dp = [0] * (l + 1)
    dp[0] = 1

    for i in range(1, l + 1):
        for a in arr:
            t = len(a)
            if i >= t:
                if s[i - t : i] == a:
                    dp[i] |= dp[i - t]

    return dp[l]

print(solution())