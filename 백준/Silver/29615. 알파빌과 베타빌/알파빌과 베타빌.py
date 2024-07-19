import sys
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    waitList = list(map(int, input().split()))
    friends = set(map(int, input().split()))

    changeCnt = 0
    for i in range(m, n):
        if waitList[i] in friends:
            changeCnt += 1

    return changeCnt

print(solution())