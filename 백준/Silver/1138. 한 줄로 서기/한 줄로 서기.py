import sys
from itertools import permutations
input = sys.stdin.readline
toStr = lambda x: str(x + 1)

def solution():
    n = int(input())
    taller = list(map(int, input().split()))
    
    for order in permutations([i for i in range(n)], n):
        if isRightOrder(order, n, taller):
            return ' '.join(map(toStr, order))

def isRightOrder(order, n, taller):
    for i in range(n - 1, -1, -1):
        leftTaller = calcLeftTaller(order, i)
        if leftTaller != taller[order[i]]:
            return False
    return True

def calcLeftTaller(order, idx):
    cnt = 0
    for i in range(idx - 1, -1, -1):
        if order[i] > order[idx]:
            cnt += 1
    return cnt

print(solution())