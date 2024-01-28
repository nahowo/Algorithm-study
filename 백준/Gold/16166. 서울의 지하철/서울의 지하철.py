import sys
input=sys.stdin.readline

n=int(input())
routeMap=dict()
connectedRoute=dict()

for i in range(1,n+1):
    tmp=list(map(int,input().split()))
    k=tmp[0]

    for j in range(1,k+1):
        routeMap[tmp[j]]=routeMap.get(tmp[j],[])+(tmp[1:])
        connectedRoute[tmp[j]]=connectedRoute.get(tmp[j],[])+[i]

destination=int(input())
visited={0}

def func(start,cnt):
    nextStations=[]
    for i in routeMap[start]:
        if i==destination:
            return cnt
        if i not in visited:
            if len(connectedRoute[i])>1:
                nextStations.append(i)
            visited.add(i)
    for i in nextStations:
        return func(i,cnt+1)

result=func(0,0)
print(result if result!=None else -1)