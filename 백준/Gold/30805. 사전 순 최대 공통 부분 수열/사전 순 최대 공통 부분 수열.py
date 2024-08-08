import sys
input = sys.stdin.readline
'''
1. (인덱스, 값) 형식으로 각 수열을 분리해 배열에 저장한다. 
2. 분리한 튜플 배열을 값 기준 내림차순, 인덱스 기준 오름차순으로 정렬한다. 
3. a용 포인터, b용 포인터를 각각 0으로 초기화한다. a용 인덱스, b용 인덱스를 각각 0으로 초기화한다. 정답 수열을 빈 배열로 초기화한다. 
    a용 포인터: 현재 보고 있는 a 수열의 원소 위치
    a용 인덱스: 정답 수열에 들어간 a의 원소 중 가장 마지막 원소의 인덱스(원래 수열에서의 원소의 위치)
4. a용 포인터가 n 이하이거나, b용 포인터가 m 이하인 경우동안 while문을 돌린다. 
    if a[a용 포인터] 값 == b[b용 포인터] 값인 경우:
        if a[a용 포인터] 인덱스 > a용 인덱스이고 b[b용 포인터] 인덱스 > b용 인덱스인 경우:
            정답 수열에 해당 값을 추가한다. 
            a, b용 포인터를 각각 1씩 증가시킨다. 
        else:
            if a[a용 포인터] 인덱스 < a용 인덱스인 경우:
                a용 포인터를 1 증가시킨다. 
            if b[b용 포인터] 인덱스 < b용 인덱스인 경우:
                b용 포인터를 1 증가시킨다. 
    else:
        if a[a용 포인터] 값 > b[b용 포인터] 값인 경우:
            a용 포인터를 1 증가시킨다. 
        if a[a용 포인터] 값 < b[b용 포인터] 값인 경우:
            b용 포인터를 1 증가시킨다. 
'''   
def solution():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))

    aArr = []
    bArr = []
    for i in range(n):
        aArr.append((i, a[i]))
    for i in range(m):
        bArr.append((i, b[i]))
    aArr.sort(key = lambda x: (-x[1], x[0]))
    bArr.sort(key = lambda x: (-x[1], x[0]))
    answer = []

    aPt, bPt, aIdx, bIdx = 0, 0, 0, 0
    while aPt < n and bPt < m:
        if aArr[aPt][1] == bArr[bPt][1]:
            if aArr[aPt][0] >= aIdx and bArr[bPt][0] >= bIdx:
                answer.append(aArr[aPt][1])
                aIdx = aArr[aPt][0]
                bIdx = bArr[bPt][0]
                aPt += 1
                bPt += 1
            elif aArr[aPt][0] < aIdx:
                aPt += 1
            elif bArr[bPt][0] < bIdx:
                bPt += 1
        else:
            if aArr[aPt][1] > bArr[bPt][1]:
                aPt += 1
            else:
                bPt += 1
    return answer

result = solution()
print(len(result))
if len(result) != 0:
    print(*result)