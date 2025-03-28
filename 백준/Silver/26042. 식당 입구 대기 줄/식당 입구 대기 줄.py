import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    answer = [0, n]
    q = deque()
    length = 0
    for i in range(n):
        tmp = list(input().rstrip().split())
        if tmp[0] == '1':
            a = int(tmp[1])
            q.append(a)
            length += 1
            if length > answer[0] or length == answer[0] and a < answer[1]:
                answer[0] = length
                answer[1] = a
        else:
            q.popleft()
            length -= 1
    return answer
    
print(*solution())