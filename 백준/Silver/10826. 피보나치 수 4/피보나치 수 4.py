import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    fibo = [0, 1]
    if n < 2:
        return fibo[n]
    for i in range(2, n + 1):
        fibo[0], fibo[1] = fibo[1], sum(fibo)
    return fibo[1]

print(solution())