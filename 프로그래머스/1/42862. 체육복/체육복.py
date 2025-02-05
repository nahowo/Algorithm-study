import heapq

def solution(n, lost, reserve):
    answer = 0
    cnt = [1] * (n + 1)
    cnt[0] = 0
    for i in reserve:
        cnt[i] += 1
    
    for i in lost:
        cnt[i] -= 1
    
    for i in range(1, n + 1):
        if cnt[i] > 0:
            continue
        if i > 1 and cnt[i - 1] == 2:
            cnt[i - 1] -= 1
            cnt[i] += 1
        elif i < n and cnt[i + 1] == 2:
            cnt[i + 1] -= 1
            cnt[i] += 1
    
    for i in range(1, n + 1):
        if cnt[i] >= 1:
            answer += 1
    
    return answer