import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    tmp = list(map(int, input().split()))
    balloons = deque()
    for i in range(1, n + 1):
        balloons.append([i, tmp[i - 1]])
    
    
    answer = []
    for i in range(n):
        x, move = balloons.popleft()
        answer.append(x)
        if balloons:
            if move > 0:
                for _ in range(move - 1):
                    balloons.append(balloons.popleft())
            else:
                for _ in range(move - 1, -1):
                    balloons.appendleft(balloons.pop())

    return answer

print(*solution())