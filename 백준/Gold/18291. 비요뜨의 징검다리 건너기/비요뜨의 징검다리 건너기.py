import sys
input = sys.stdin.readline
DIV = 10 ** 9 + 7

def solution(n: int) -> int:
    if n == 1:
        return 1
    return power(n - 2)

def power(n: int) -> int:
    if n < 2:
        return (2 ** n) % DIV
    half = n // 2
    if n % 2 == 0:
        return (power(half) ** 2) % DIV
    return (power(half) ** 2 * 2) % DIV

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))