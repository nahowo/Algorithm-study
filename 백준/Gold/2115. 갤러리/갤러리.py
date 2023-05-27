import sys
input=sys.stdin.readline
n,m=map(int,input().split())
map=[input().rstrip() for _ in range(n)]
check=[[([0]*4) for _ in range(m)] for _ in range(n)] #[위,아래,왼쪽,오른쪽]
answer=0
def func(y,x):
    global answer
    if map[y][x]==".":
        if map[y+1][x]==".":
            if map[y][x-1]=="X" and map[y+1][x-1]=="X" and check[y][x][0]==0 and check[y+1][x][0]==0:
                check[y][x][0]=check[y+1][x][0]=check[y][x-1][1]=check[y+1][x-1][1]=1 #겹치는 부분도 한번에 1로 처리
                answer+=1
            if map[y][x+1]=="X" and map[y+1][x+1]=="X" and check[y][x][1]==0 and check[y+1][x][1]==0:
                check[y][x][1]=check[y+1][x][1]=check[y][x+1][0]=check[y+1][x+1][0]=1
                answer+=1
        if map[y][x+1]==".":
            if map[y-1][x]=="X" and map[y-1][x+1]=="X" and check[y][x][2]==0 and check[y][x+1][2]==0:
                check[y][x][2]=check[y][x+1][2]=check[y-1][x][3]=check[y-1][x+1][3]=1
                answer+=1
            if map[y+1][x]=="X" and map[y+1][x+1]=="X" and check[y][x][3]==0 and check[y][x+1][3]==0:
                check[y][x][3]=check[y][x+1][3]=check[y+1][x][2]=check[y+1][x+1][2]=1
                answer+=1
for i in range(1,n-1):
        for j in range(1,m-1):
            func(i,j)
print(answer)