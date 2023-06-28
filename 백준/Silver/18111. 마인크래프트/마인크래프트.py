from collections import Counter
n,m,b=map(int,input().split())
ground=[]
for i in range(n):
    ground.extend(list(map(int,input().split())))
minh=min(ground)
maxh=max(ground)
sumh=sum(ground)
time=1000000000000000
ground=dict(Counter(ground))
for i in range(minh,maxh+1):
    if sumh+b>=i*n*m:
        t=0
        for k in ground:
            if k>i:
                t+=(k-i)*ground[k]*2
            elif k<i:
                t+=(i-k)*ground[k]
        if t <= time:
            time=t
            height=i
print(time,height)
