import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    
    return gcd(b, a % b)

def solution():
    a, b = sorted(map(int, input().split()))
    return gcd(a, b) * "1"

print(solution())