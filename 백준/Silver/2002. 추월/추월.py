import sys
input = sys.stdin.readline

def isSkipped(idx, before, after):
    for bIdx in range(idx):
        if after[before[idx]] < after[before[bIdx]]:
            return False
    return True

def solution():
    n = int(input())
    before = dict()
    after = dict()
    for idx in range(n):
        number = input().rstrip()
        before[idx] = number
    
    for idx in range(n):
        number = input().rstrip()
        after[number] = idx
    
    skipped = 0
    for idx in range(n):
        if not isSkipped(idx, before, after):
            skipped += 1

    return skipped

print(solution())