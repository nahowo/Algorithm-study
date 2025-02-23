import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    road = [0] + list(map(int, input().split()))
    price = list(map(int, input().split()))
    current = price[0]
    totalPrice = 0
    for i in range(1, n):
        totalPrice += road[i] * current
        current = min(current, price[i])
    return totalPrice

print(solution())