import sys
from collections import deque
input = sys.stdin.readline

def solution():
    global n, q
    n, m = map(int, input().split())
    q = deque([i for i in range(1, n + 1)])
    targets = list(map(int, input().split()))
    answer = 0

    for x in targets:
        direction = calcDirection(x)
        tmp = rotate(x, direction)
        answer += tmp
    return answer

def calcDirection(x):
    left = 0
    right = 0
    for i in range(len(q)):
        left += 1
        if q[i] == x:
            break
    for i in range(len(q) - 1, -1, -1):
        right += 1
        if q[i] == x:
            right += 1
            break

    if left < right:
        return 0
    else:
        return 1
    
def rotate(target, direction):
    dist = 0
    while True:
        if q[0] == target:
            q.popleft()
            break
        if direction == 0:
            x = q.popleft()
            q.append(x)
        else:
            x = q.pop()
            q.appendleft(x)
        dist += 1
    return dist

print(solution())