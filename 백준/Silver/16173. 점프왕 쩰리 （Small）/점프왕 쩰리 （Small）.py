import sys
input=sys.stdin.readline
n=int(input())
gameboard=[]
for _ in range(n):
    gameboard.append(list(map(int,input().split())))
def dfs(x,y):
    if x>=n or y>=n:
        return False
    elif x==n-1 and y==n-1:
        return True
    step=gameboard[x][y]
    if step==0:
        return False
    if dfs(x,y+step) or dfs(x+step,y):
        return True
    return False
if dfs(0,0)==False:
    print("Hing")
else:
    print("HaruHaru")