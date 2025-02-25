import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    fibo = [1] * (n + 1)
    fibo[0] = 0

    for i in range(3, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    return fibo[n]

print(solution())