import sys
input = sys.stdin.readline
MAX_SIZE = 10 ** 5

def solution():
    n = int(input())
    coins = [MAX_SIZE] * (n + 5)
    coins[2] = coins[5] = 1

    for i in range(n + 1):
        if i - 2 >= 0:
            coins[i] = min(coins[i], coins[i - 2] + 1)
        if i - 5 >= 0:
            coins[i] = min(coins[i], coins[i - 5] + 1)

    if coins[n] == MAX_SIZE:
        return -1
    return coins[n]

print(solution())