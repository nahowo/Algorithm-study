import sys
input = sys.stdin.readline

def solution():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    meal = 0
    left = 0

    for i in range(n):
        tmpMeal = a[i] // x
        meal += tmpMeal
        tmpLeft = a[i] % x
        left += max(tmpLeft - (tmpMeal * (y - x)), 0)

    print(meal)
    print(left)
    return

solution()