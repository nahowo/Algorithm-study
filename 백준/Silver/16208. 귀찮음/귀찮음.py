import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    sticks = list(map(int,input().split()))
    sticks.sort()
    price = 0
    length = sum(sticks)

    for i in range(n):
        length -= sticks[i]
        price += length * sticks[i]
    return price

print(solution())