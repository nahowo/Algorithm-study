import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def move(a, b):
    a, b = sorted([a, b])
    if a == b:
        return 1
    if a == 0:
        return 2
    if b - a == 2:
        return 4
    return 3

def recursion(n, command, l, r):
    if n == N - 1:
        return min(move(l, command[n]), move(r, command[n]))

    if cache[n][l][r] != -1:
        return cache[n][l][r]
    
    moveL = (move(l, command[n]) + recursion(n + 1, command, command[n], r))
    moveR = (move(r, command[n]) + recursion(n + 1, command, l, command[n]))
    cache[n][l][r] = min(moveL, moveR)
    return cache[n][l][r]

def solution():
    global N, cache
    command = list(map(int, input().split()))
    N = len(command) - 1
    cache = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(N)] # n번째 단계에서 왼발, 오른발 위치 캐싱
    return recursion(0, command, 0, 0)

print(solution())