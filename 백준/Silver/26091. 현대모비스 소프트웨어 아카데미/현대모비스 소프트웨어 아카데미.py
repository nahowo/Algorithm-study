import sys
input=sys.stdin.readline

def func():
    n,m=map(int,input().split())
    skill=list(map(int,input().split()))
    skill.sort()
    visited=set()

    team=0
    start=0
    end=n-1
    while True:
        if end==0 or start==n or end==start:
            break
        if start not in visited:
            if skill[start]+skill[end]>=m:
                team+=1
                visited.add(end)
                visited.add(start)
                end-=1
                start+=1
            else:
                start+=1
        else:
            start+=1
                
    return team
print(func())