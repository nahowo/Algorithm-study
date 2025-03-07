def solution(cap, n, deliveries, pickups):
    answer = 0
    dsum = 0
    psum = 0
    
    for i in range(n - 1, -1, -1):
        cnt = 0
        dsum += deliveries[i]
        psum += pickups[i]
        
        while dsum > 0 or psum > 0:
            dsum -= cap
            psum -= cap
            cnt += 1
        answer += (i + 1) * 2 * cnt
        
    return answer