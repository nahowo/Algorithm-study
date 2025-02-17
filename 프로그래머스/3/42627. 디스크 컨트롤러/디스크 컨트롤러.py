import heapq

def solution(jobs):
    answer = 0
    n = len(jobs)
    for i in range(n):
        jobs[i].append(i) # 작업번호 부여
    jobs.sort() # 요청시간 기준 정렬
    hd = 0
    rq = [] # [소요시간, 요청시간, 작업번호]
    idx = 0
    
    for time in range(501001):
        while idx < n:
            if jobs[idx][0] == time:
                heapq.heappush(rq, [jobs[idx][1], jobs[idx][0], jobs[idx][2]])
                idx += 1
            else:
                break
        if hd > 0:
            hd -= 1
        if hd == 0 and rq:
            duration, request, num = heapq.heappop(rq)
            answer += time + duration - request
            hd = duration
    
    return answer // n