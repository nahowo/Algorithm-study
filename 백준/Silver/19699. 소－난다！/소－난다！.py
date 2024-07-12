import sys
input = sys.stdin.readline
from itertools import combinations

def isPrimeNumber(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False
    return True

def sumH(combi):
    s = 0
    for i in range(n):
        if i in combi:
            s += h[i]
    return s

def solution():
    combination = combinations(range(n), m)
    for combi in combination:
        tmpSum = sumH(combi)
        if isPrimeNumber(tmpSum) == True:
            primeSums.add(tmpSum)
    
n, m = map(int, input().split())
h = list(map(int, input().split()))
primeSums = set()

solution()
primeSums = sorted(list(primeSums))
if len(primeSums) == 0:
    print(-1)
else:
    print(' '.join(list(map(str, primeSums))))