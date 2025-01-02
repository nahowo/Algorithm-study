import sys
input = sys.stdin.readline

isOdd = lambda i: (i % 2)

def solution():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    maxLen = 0
    l, r = 0, 0
    oddCnt = 0
    while r < n:
        if oddCnt < k:
            if isOdd(s[r]):
                oddCnt += 1
            r += 1
            maxLen = max(maxLen, r - l - oddCnt)
        elif not isOdd(s[r]):
            r += 1
            maxLen = max(maxLen, r - l - oddCnt)
        else:
            if isOdd(s[l]):
                oddCnt -= 1
            l += 1

    return maxLen

print(solution())