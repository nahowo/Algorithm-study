import sys
from collections import deque
input = sys.stdin.readline

def solution():
    global n, k
    n, k = map(int, input().split())
    sx = ''.join(input().rstrip().split())

    visited = dict()
    q = deque([sx])
    visited[sx] = 0
    while q:
        x = q.popleft()
        if check(x):
            return visited[x]
        for idx in range(0, n - k + 1):
            nx = convert(x, idx)
            if nx not in visited:
                visited[nx] = visited[x] + 1
                q.append(nx)
    return -1

def convert(perm, idx):
    arr = list(perm)
    for i in range(k // 2):
        start = i + idx
        end = idx + k - i - 1
        arr[start], arr[end] = arr[end], arr[start]
    return ''.join(arr)

def check(perm):
    for i in range(1, n + 1):
        if perm[i - 1] != str(i):
            return False
    return True

print(solution())