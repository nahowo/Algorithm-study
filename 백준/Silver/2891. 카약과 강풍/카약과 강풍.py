import sys
input = sys.stdin.readline


def solution():
    n, s, r = map(int, input().split())
    minC = s
    damaged = list(map(int, input().split()))
    canB = set(list(map(int, input().split())))
    cnt = 0

    boat = [1] * (n + 2)
    for i in damaged:
        boat[i] -= 1
    for i in canB:
        boat[i] += 1

    for i in range(1, n + 1):
        if boat[i] == 0:
            if boat[i - 1] == 2:
                boat[i - 1] -= 1
                boat[i] += 1
            elif boat[i + 1] == 2:
                boat[i + 1] -= 1
                boat[i] += 1
            else:
                cnt += 1
    return cnt

print(solution())