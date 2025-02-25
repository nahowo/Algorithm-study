import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    fibo = [1] * (n + 3)
    fibo[1] = fibo[2] = fibo[3] = 1

    for i in range(4, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 3]

    return fibo[n]

print(solution())