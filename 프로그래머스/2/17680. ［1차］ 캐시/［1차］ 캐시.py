from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    
    for i in cities:
        i = i.lower()
        # 실행시간 계산
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
        else:
            answer += 5
            # 캐시 교체
            cache.append(i)
            if len(cache) > cacheSize:
                cache.popleft()
        
    return answer