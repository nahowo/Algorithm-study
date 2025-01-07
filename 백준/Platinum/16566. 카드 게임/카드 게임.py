import sys
input = sys.stdin.readline

def find(x):
    if x != next[x]:
        next[x] = find(next[x])
    return next[x]

def union(a, b):
    if b >= m:
        return
    
    a = find(a)
    b = find(b)
    next[a] = b

def binarySearch(target, arr):
    start = 0
    end = m - 1

    answer = m
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return answer

def solution():
    global next, m
    n, m, k = map(int, input().split())
    minsu = list(map(int, input().split()))
    chulsu = list(map(int, input().split()))
    minsu.sort()
    next = [i for i in range(m)]

    for i in range(k):
        idx = binarySearch(chulsu[i], minsu)
        idx = find(idx)
        print(minsu[idx])
        union(idx, idx + 1)
    
solution()