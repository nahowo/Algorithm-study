import heapq
def solution(A, B):
    answer = 0
    heapq.heapify(B)
    A.sort()
    
    for a in A:
        while B:
            b = heapq.heappop(B)
            if b > a:
                answer += 1
                break
    
    return answer