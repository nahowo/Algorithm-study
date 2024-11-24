import sys
input = sys.stdin.readline

def getPrimes(n):
    primes = [True] * (n + 1)
    primes[0], primes[1] = False, False

    for i in range(2, int(n ** (1 / 2)) + 1):
        if primes[i]:
            for j in range(2, int(n / i + 1)):
                primes[i * j] = False

    return primes

def getTwoElements(n, primes):
    a = n // 2
    b = n // 2

    while a > 1:
        if primes[a] and primes[b] and a + b == n:
            return [a, b]
        a -= 1
        b += 1

def solution():
    n = int(input())
    if n < 8: # 소수 4개로 만들 수 있는 가장 작은 수는 8(2 + 2 + 2 + 2)
        return [-1]

    if n % 2 == 0:
        elements = [2, 2] # 짝수 n은 소수 2 + 2 + a + b로 구성(a + b = n - 4)
        n -= 4
    else:
        elements = [2, 3] # 홀수 n은 소수 2 + 3 + a + b로 구성(a + b = n - 5)
        n -= 5

    primes = getPrimes(n)
    twoElements = getTwoElements(n, primes)
    elements.extend(twoElements)
    return elements

print(*solution())