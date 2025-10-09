import sys
from collections import deque
input = sys.stdin.readline

def solution():
    n = int(input())
    dq = deque()
    answer = list()
    for _ in range(n):
        tmp = input().split()
        cmd = tmp[0]
        x = tmp[-1]
        if cmd == '1':
            dq.appendleft(x)
        elif cmd == '2':
            dq.append(x)
        elif cmd == '3':
            if isEmpty(dq):
                answer.append('-1')
            else:
                answer.append(dq.popleft())
        elif cmd == '4':
            if isEmpty(dq):
                answer.append('-1')
            else:
                answer.append(dq.pop())
        elif cmd == '5':
            answer.append(str(len(dq)))
        elif cmd == '6':
            if isEmpty(dq):
                answer.append('1')
            else:
                answer.append('0')
        elif cmd == '7':
            if isEmpty(dq):
                answer.append('-1')
            else:
                answer.append(dq[0])
        elif cmd == '8':
            if isEmpty(dq):
                answer.append('-1')
            else:
                answer.append(dq[-1])
    return '\n'.join(answer)

def isEmpty(dq):
    if len(dq) == 0:
        return True
    return False

print(solution())