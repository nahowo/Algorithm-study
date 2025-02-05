import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def getSum(x):
    if x <= 0:
        return 0
    
    times = int(math.log2(x))
    nx = 2 ** times
    if nx == x:
        return times * x // 2 + 1
    
    diff = x - nx
    return getSum(nx) + diff + getSum(diff)

def solution():
    a, b = map(int, input().split())
    return getSum(b) - getSum(a - 1)

print(solution())