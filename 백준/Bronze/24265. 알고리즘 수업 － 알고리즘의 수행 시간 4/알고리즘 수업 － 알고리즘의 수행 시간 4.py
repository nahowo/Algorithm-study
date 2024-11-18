import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    print(n * (n- 1) // 2)
    print(2) # 다항식은 f(n) = n * (n - 1) / 2 = (n / 2) ^ 2 - (n / 2)
    return

solution()