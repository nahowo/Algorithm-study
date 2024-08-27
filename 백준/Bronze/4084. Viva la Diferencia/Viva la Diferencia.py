import sys
input = sys.stdin.readline

def solution(a, b, c, d):
    cnt = 0
    while True:
        if a == b and b == c and c == d:
            return cnt

        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        cnt += 1

while True:
    a, b, c, d = map(int, input().split())
    if a == 0 and b == 0 and c == 0 and d == 0:
        break
    print(solution(a, b, c, d))