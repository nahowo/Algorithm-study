import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    structTypes = list(input().split())
    dq = deque()
    data = list(input().split())
    for i in range(n):
        if structTypes[i] == '0':
            dq.append(data[i])
    
    answer = list()
    m = int(input())
    c = list(input().split())
    for i in range(m):
        dq.appendleft(c[i])
        answer.append(dq.pop())
    
    return ' '.join(answer)

print(solution())