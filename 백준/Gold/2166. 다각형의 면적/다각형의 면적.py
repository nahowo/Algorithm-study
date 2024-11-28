import sys
input = sys.stdin.readline

def getSum(start):
    s = 0
    first = dots[0][start]
    for i in range(1, n + 1):
        first *= dots[i][not start]
        s += first
        first = dots[i][start]
    return s

def solution():
    global n, dots
    n = int(input())

    dots = []
    for _ in range(n):
        dots.append(list(map(int, input().split())))
    dots.append(dots[0])

    f1 = getSum(0)
    f2 = getSum(1)
    plane = abs(f1 - f2) / 2
    return round(plane + 0.0000000001, 1)

print(solution())