import sys
input = sys.stdin.readline

def solution():
    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort(reverse = True)
    day = 0
    for i in range(1, n + 1):
        toGrow = i + trees[i - 1]
        day = max(day, toGrow)
    return day + 1

print(solution())