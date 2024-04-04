import sys
import heapq
input=sys.stdin.readline

def func():
    n,m,k=map(int,input().split())
    beer=[]
    hq=[]
    for _ in range(k):
        beer.append(list(map(int,input().split()))) # [선호도, 도수]
    beer.sort(key=lambda x:x[1])

    need=0 # 채워야 하는 선호도 합
    for i in beer:
        if len(hq)<n:
            heapq.heappush(hq,i)
            need+=i[0] # 선호도 추가
            if len(hq)==n:
                if need>=m: # 선호도 조건 만족 시 종료
                    return i[1] # 조건을 만족하는 가장 낮은 간 레벨
                else:
                    need-=heapq.heappop(hq)[0] # 선호도 제거
    return -1

print(func())