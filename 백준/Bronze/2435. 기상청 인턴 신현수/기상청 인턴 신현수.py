import sys
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    temp = list(map(int, input().split())) + [0]
    maxTemp = -100 * n

    for i in range(n - k + 1):
        maxTemp = max(sum(temp[i : i + k]), maxTemp)
    return maxTemp

print(solution())