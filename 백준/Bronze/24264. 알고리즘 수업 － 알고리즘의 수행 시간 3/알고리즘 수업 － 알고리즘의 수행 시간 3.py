import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    print(n ** 2) # for문은 n번만큼 반복
    print(2) # 다항식은 f(n) = n ^ 2, 즉 다항식의 최고차항의 차수는 항상 2
    return

solution()