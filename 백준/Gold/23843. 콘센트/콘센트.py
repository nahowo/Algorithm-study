import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    t=list(map(int,input().split()))
    t.sort()
    concent=[0]*m

    if m==1:
        return sum(t)

    while t:
        x=t.pop()
        n-=1
        concent[0]+=x
        k=1 # 충전할 콘센트 위치 인덱스
        for i in range(n-1,-1,-1):
            if concent[k]+t[i]<=concent[0]:
                nx=t.pop()
                n-=1
                concent[k]+=nx
            else:
                if k==m-1:
                    continue
                else:
                    nx=t.pop()
                    n-=1
                    k+=1
                    concent[k]+=nx
    return concent[0]
        
print(func())