from collections import deque
from math import ceil
def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    q = deque()
    for i in range(n):
        q.append([progresses[i], speeds[i]])
    
    while q:
        p, s = q.popleft()
        day = ceil((100 - p) / s)
        cnt = 1
        while q:
            if q[0][0] + q[0][1] * day >= 100:
                q.popleft()
                cnt += 1
            else:
                break
        answer.append(cnt)
    
    return answer