import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    num = set(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))
    answer = ['0'] * m
    for i in range(m):
        if q[i] in num:
            answer[i] = '1'
    return '\n'.join(answer)

t = int(input())
for _ in range(t):
    print(solution())