import sys
input = sys.stdin.readline

def getSumArray(arr, n):
    sumArr = [arr[0]]
    for i in range(n):
        sumArr.append(sumArr[i] + arr[i])
    
    return sumArr

def getPartialArray(arr, n):
    partial = dict()
    for i in range(1, n + 1): # 부분배열 길이
        for j in range(i, n + 1): # 부분배열 끝 인덱스
            tmp = arr[j] - arr[j - i]
            partial[tmp] = partial.get(tmp, 0) + 1
    return partial

def solution():
    t = int(input())
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    aSum = getSumArray(a, n)
    bSum = getSumArray(b, m)
    aPartial = getPartialArray(aSum, n)
    bPartial = getPartialArray(bSum, m)

    cnt = 0
    for ai in aPartial.keys():
        if t - ai in bPartial:
            cnt += aPartial[ai] * bPartial[t - ai]
    return cnt

print(solution())