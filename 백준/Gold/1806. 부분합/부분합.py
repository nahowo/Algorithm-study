import sys
input = sys.stdin.readline

def solution():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    start, end = 0, 0
    if sum(arr) < s:
        return 0
    
    tmpSum = arr[0]
    answer = 100001
    while True:
        if tmpSum < s:
            end += 1
            if end == n:
                break
            tmpSum += arr[end]
        else:
            tmpSum -= arr[start]
            answer = min(answer, end - start + 1)
            start += 1
    
    return answer

print(solution())