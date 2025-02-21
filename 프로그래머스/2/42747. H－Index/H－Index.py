import bisect

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()
    for h in range(n + 1):
        idx = bisect.bisect_left(citations, h)
        if n - idx >= h:
            answer = h
            
    return answer