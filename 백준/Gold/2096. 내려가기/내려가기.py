import sys
input=sys.stdin.readline

def func():
    n=int(input())
    lines=[]
    INF=10**6
    maxprev=minprev=list(map(int,input().split())) # 첫 번째 줄
    for _ in range(n-1):
        line=list(map(int,input().split()))
        maxLine=[0]*3
        minLine=[0]*3
        for i in range(3):
            mintmp=[]
            maxtmp=[]
            for j in [i-1,i,i+1]:
                if 0<=j<3:
                    mintmp.append(minprev[j])
                    maxtmp.append(maxprev[j])
            maxLine[i]=max(maxtmp)+line[i]
            minLine[i]=min(mintmp)+line[i]
        maxprev=maxLine
        minprev=minLine

    maxPoint=max(maxprev)
    minPoint=min(minprev)
    print(maxPoint,minPoint)
    return
    
func()