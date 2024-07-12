import sys
input = sys.stdin.readline

def solution(n, b, m):
    year = 0
    while True:
        if n > m:
            return year
        n += n * b / 100
        year += 1

while True:
    try:
        n, b, m = map(float, input().split())
        print(solution(n, b, m))
    except:
        break