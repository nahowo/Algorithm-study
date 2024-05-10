import sys
input=sys.stdin.readline

def func():
    n,m,k=map(int,input().split())
    best=dict()
    for i in range(1,n+1):
        best[i]=0
    for _ in range(m):
        tmp=list(map(float,input().split()))
        for i in range(0,len(tmp),2):
            candidate=int(tmp[i])
            score=tmp[i+1]
            if score>best[candidate]:
                best[candidate]=score

    total_score=list(best.values())
    total_score.sort(reverse=True)
    return round(sum(total_score[:k]),1)

print(func())