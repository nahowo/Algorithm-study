import sys
input = sys.stdin.readline
MIN_SIZE = -1 * 10 ** 9 - 1

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

    tmpLis = [MIN_SIZE] # 정렬된 상태로 유지, 패딩 설정
    pos = [0] # lis에 들어갈 원소의 위치

    idx = 1
    for i in range(n):
        if a[i] > tmpLis[-1]:
            tmpLis.append(a[i])
            pos.append(idx)
            idx += 1
        else:
            tmpIdx = binarySearch(a[i], tmpLis)
            tmpLis[tmpIdx] = a[i]
            pos.append(tmpIdx)
    
    idx = len(tmpLis) - 1
    lis = [0] * idx
    for i in range(n, 0, -1):
        if idx == 0:
            break
        if pos[i] == idx:
            lis[idx - 1] = a[i - 1]
            idx -= 1

    print(len(lis))
    print(*lis)
    return

solution()