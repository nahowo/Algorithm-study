import sys
input = sys.stdin.readline

def sumOfFactors(n):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    return s

def solution():
    t = int(input())
    numbers = list(map(int, input().split()))

    for n in numbers:
        result = sumOfFactors(n)
        if n == result:
            print("Perfect")
        elif n > result:
            print("Deficient")
        else:
            print("Abundant")

solution()