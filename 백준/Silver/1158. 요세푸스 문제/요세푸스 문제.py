import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    q = deque(list(range(1, n + 1)))
    answer = [0] * n

    for i in range(n):
        for j in range(k - 1):
            q.append(q.popleft())
        answer[i] = q.popleft()
    return '<' + ', '.join(map(str, answer)) + '>'

print(solution())