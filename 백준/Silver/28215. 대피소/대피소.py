# import sys
# input = sys.stdin.readline
# from itertools import combinations

# def distance(a, b):
#     return abs(a[0] - b[0]) + abs(a[1] - b[1])

# def solution(combi):
#     tmpMax = 0
#     for i in range(n):
#         tmpMin = sys.maxsize
#         for j in combi:
#             dist = distance(houese[i], houese[j])
#             tmpMin = min(dist, tmpMin)
#         tmpMax = max(tmpMin, tmpMax)
#     return tmpMax


# n, k = map(int,input().split())
# houese = []
# for i in range(n):
#     houese.append(list(map(int, input().split())))

# maxLength = sys.maxsize
# for combi in combinations(range(n), k):
#     maxLength = min(maxLength, solution(combi))

# print(maxLength)

import sys
input = sys.stdin.readline
from itertools import combinations

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def combination(c, s, cnt):
    if cnt == k:
        combi.append(c.copy())
        return
    
    for i in range(s, n):
        if i not in c:
            c.append(i)
            combination(c, i + 1, cnt + 1)
            c.pop()

def solution(combi):
    tmpMax = 0
    for i in range(n):
        tmpMin = sys.maxsize
        for j in combi:
            dist = distance(houese[i], houese[j])
            tmpMin = min(dist, tmpMin)
        tmpMax = max(tmpMin, tmpMax)
    return tmpMax


n, k = map(int,input().split())
houese = []
for i in range(n):
    houese.append(list(map(int, input().split())))
combi = []
combination([], 0, 0)

maxLength = sys.maxsize
for c in combi:
    maxLength = min(maxLength, solution(c))

print(maxLength)