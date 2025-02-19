import heapq

def solution(routes):
    answer = 0
    heapq.heapify(routes)
    
    while routes:
        sx, ex = heapq.heappop(routes)
        while routes:
            if routes[0][0] <= ex:
                if routes[0][1] < ex:
                    ex = routes[0][1]
                heapq.heappop(routes)
            else:
                break
        answer += 1
        
    return answer