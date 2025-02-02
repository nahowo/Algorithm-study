import sys
from math import comb
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    return comb(m, n)

t = int(input())
for _ in range(t):
    print(solution())