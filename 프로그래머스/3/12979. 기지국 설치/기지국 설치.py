def solution(n, stations, w):
    answer = 0
    stations.sort()
    m = len(stations)
    s = max(1, stations[0] - w)
    e = min(n, stations[0] + w)
    filled = [] # 이미 전파가 전달되는 공간 [[start, end], ...]
    for i in range(1, m):
        cs = max(1, stations[i] - w)
        ce = min(n, stations[i] + w)
        if e >= cs: # 이전 공간과 겹친다면
            e = ce
        else:
            filled.append([s, e])
            s, e = cs, ce
    filled.append([s, e])
    filled.append([n + 1, n + 1])
    
    start = 1
    for s, e in filled:
        end = s
        dist = end - start # 빈 공간의 거리
        if dist % (2 * w + 1) == 0:
            answer += dist // (2 * w + 1)
        else:
            answer += dist // (2 * w + 1) + 1
        start = e + 1
    
    return answer