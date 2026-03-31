import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    for i in range(n, 0, -1):
        print('*' * i)

solution()