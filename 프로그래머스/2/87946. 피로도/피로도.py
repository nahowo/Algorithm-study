from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    perm = list(permutations([i for i in range(len(dungeons))]))
    for i in range(len(perm)):
        route = perm[i]
        cnt = 0
        tmpK = k
        for r in route:
            if tmpK >= dungeons[r][0]:
                tmpK -= dungeons[r][1]
                cnt += 1
        answer = max(answer, cnt)
        
    return answer