import sys
from itertools import combinations
input = sys.stdin.readline

def solution():
    n, k = map(int, input().split())
    learned = {'a', 'n', 't', 'i', 'c'}
    word = [set() for _ in range(n)]
    total = set()

    for i in range(n):
        w = input().rstrip()
        for j in w:
            if j not in learned:
                word[i].add(j)
                total.add(j)

    if k < 5:
        return 0
    if len(total) <= k - 5:
        return n
    answer = 0
    for c in combinations(total, k - 5):
        answer = max(answer, check(c, learned.copy(), word))
    return answer

def check(c, learned, word):
    for i in c:
        learned.add(i)
    cnt = 0
    for w in word:
        if w.issubset(learned):
            cnt += 1
    return cnt

print(solution())