import heapq

def solution(operations):
    answer = [0, 0]
    minq = []
    maxq = []
    d = dict()
    cnt = 0
    
    for i in operations:
        cmd, num = i.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)
            d[num] = d.get(num, 0) + 1
            cnt += 1
        else:
            if cnt > 0:
                if num == -1:
                    while minq and d[minq[0]] < 1:
                        x = heapq.heappop(minq)
                    d[heapq.heappop(minq)] -= 1
                
                else:
                    while maxq and d[-maxq[0]] < 1:
                        x = heapq.heappop(maxq)
                    d[-heapq.heappop(maxq)] -= 1
                cnt -= 1
                
    if cnt > 0:
        while maxq and d[-maxq[0]] < 1:
            x = heapq.heappop(maxq)
        answer[0] = -maxq[0]
        while minq and d[minq[0]] < 1:
            x = heapq.heappop(minq)
        answer[1] = minq[0]
    
    return answer