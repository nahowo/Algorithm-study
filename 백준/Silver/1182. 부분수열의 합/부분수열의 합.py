import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    answer = 0
    n, s = map(int, input().split())
    num = list(map(int, input().split()))
    for i in range(1, n + 1):
        for comb in combinations(num, i):
            if sum(comb) == s:
                answer += 1
    return answer

print(solution())