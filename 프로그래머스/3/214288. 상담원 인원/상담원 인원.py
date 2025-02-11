import heapq

def calcTime(mento, reqs):
    waitT = 0
    for rq, length in reqs:
        minT = heapq.heappop(mento)
        waitT += max(0, minT - rq)
        heapq.heappush(mento, max(minT, rq) + length)
    return waitT

def solution(k, n, reqs):
    answer = 0
    type = {i: [] for i in range(k)}
    
    for i in range(len(reqs)):
        type[reqs[i][2] - 1].append([reqs[i][0], reqs[i][1]])

    mentos = [[0, 1] for _ in range(k)] # 대기시간 합, 해당 유형 멘토 수
    n -= k
    for i in range(k):
        mentos[i][0] = calcTime([0], type[i])
        
    for i in range(n):
        maxR = 0 # 가장 많이 감소한 대기시간
        idx = 0
        for j in range(k):
            tmp = calcTime([0] * (mentos[j][1] + 1), type[j])
            if maxR < mentos[j][0] - tmp:
                maxR = mentos[j][0] - tmp
                idx = j
        mentos[idx][1] += 1
        mentos[idx][0] -= maxR
    
    for i in range(k):
        answer += mentos[i][0]
    
    return answer