import sys
input = sys.stdin.readline

def getPrimes(n):
    arr = [True] * (n + 1)
    for i in range(2, int(n ** (1 / 2)) + 1):
        if arr[i] == True:
            for j in range(i * i, n + 1, i):
                arr[j] = False

    primes = []
    for i in range(2, n + 1):
        if arr[i] == True:
            primes.append(i)
    return primes

def solution():
    n = int(input())

    if n == 1:
        return 0
    if n == 2:
        return 1

    primes = getPrimes(n)
    cnt = 0
    start, end = len(primes) - 1, len(primes) - 1
    s = 0
    if primes[end] == n: # n이 소수인 경우
        start -= 1
        end -= 1
        cnt += 1
    s += primes[start]
    
    while start and end:
        if s > n:
            s -= primes[end]
            end -= 1
        elif s < n:
            start -= 1
            s += primes[start]
        else:
            cnt += 1
            s -= primes[end]
            end -= 1
    if s == n:
        cnt += 1
    
    return cnt

print(solution())