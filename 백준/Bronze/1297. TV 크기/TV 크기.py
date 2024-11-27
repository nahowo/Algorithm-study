import sys
input = sys.stdin.readline

def solution():
    d, h, w = map(int, input().split())

    x = (d ** 2 / (h ** 2 + w ** 2)) ** (1 / 2)
    return [int(h * x), int(w * x)]

print(*solution())