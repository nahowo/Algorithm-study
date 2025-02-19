import sys
import bisect
input = sys.stdin.readline

def solution():
    n, m = map(int, input().split())
    answer = [0] * m
    dots = list(map(int, input().split()))
    dots.sort()

    for i in range(m):
        a, b = map(int, input().split())
        start = bisect.bisect_left(dots, a)
        end = bisect.bisect_right(dots, b)
        answer[i] = end - start
    for i in answer:
        print(i)

solution()