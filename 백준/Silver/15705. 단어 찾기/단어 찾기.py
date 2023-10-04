import sys
input=sys.stdin.readline
from collections import deque
s=input().rstrip()
n,m=map(int,input().split())
graph=[]
for i in range(m):
    graph.append(input().rstrip())
d=[[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
# 8방향으로 고정해서 s길이만큼 탐색:
# 8*100*100*100 = 8,000,000
def func():
    if m<len(s) and n<len(s):
        return 0
    for x in range(m):
        for y in range(n):
            for dx,dy in d:
                tx,ty=x,y
                cnt=0
                for i in range(len(s)):
                    if 0<=tx<m and 0<=ty<n:
                        if graph[tx][ty]==s[i]:
                            tx+=dx
                            ty+=dy
                            cnt+=1
                        else:
                            break
                if cnt==len(s):
                    return 1
    return 0
print(func())