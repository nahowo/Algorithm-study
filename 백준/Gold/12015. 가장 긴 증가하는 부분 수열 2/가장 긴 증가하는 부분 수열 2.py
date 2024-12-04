import sys
input = sys.stdin.readline

def binarySearch(target, arr): # target <= arr[-1]이 보장, arr은 정렬된 상태
    s = 0
    e = len(arr) - 1
    idx = 0

    while s <= e:
        m = (s + e) // 2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            idx = m
            e = m - 1
        elif arr[m] < target:
            s = m + 1
    return idx

def solution():
    n = int(input())
    a = list(map(int, input().split()))

    lis = [0] # 정렬된 상태로 유지, 패딩 설정

    for i in range(n):
        if a[i] > lis[-1]:
            lis.append(a[i])
        else:
            idx = binarySearch(a[i], lis)
            lis[idx] = a[i]
    
    return len(lis) - 1

print(solution())