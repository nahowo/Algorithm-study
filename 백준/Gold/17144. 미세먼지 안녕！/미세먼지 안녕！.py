import sys
input=sys.stdin.readline
d=[(-1,0),(1,0),(0,-1),(0,1)]

r,c,t=map(int,input().split())
board=[]
air=[]
for i in range(r):
    tmp=list(map(int,input().split()))
    if tmp[0]==-1:
        air.append(i)
    board.append(tmp)

def dust(): # 미세먼지 확산 계산
    global board
    tBoard=[[0]*(c) for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y]>4: # 미세먼지 양이 4 이하인 경우 확산 X
                cnt=0
                for dx,dy in d:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<r and 0<=ny<c and board[nx][ny]!=-1:
                        tBoard[nx][ny]+=board[x][y]//5
                        cnt+=1
                tBoard[x][y]-=board[x][y]//5*cnt
    
    for i in range(r):
        for j in range(c):
            board[i][j]+=tBoard[i][j]

def airPurify():
    global board
    airP=air[0] # 위 공기청정기 위치
    for i in range(airP-2,-1,-1): # 아래 방향으로 미세먼지가 이동
        board[i+1][0]=board[i][0]
    
    for i in range(1,c): # 왼쪽 방향으로 미세먼지가 이동
        board[0][i-1]=board[0][i]

    for i in range(1,airP+1): # 위 방향으로 미세먼지가 이동
        board[i-1][c-1]=board[i][c-1]

    for i in range(c-1,1,-1): # 오른쪽 방향으로 미세먼지가 이동
        board[airP][i]=board[airP][i-1]
    board[airP][1]=0 # 공기청정기에서 나오는 공기

    airP=air[1] # 아래 공기청정기
    for i in range(airP+1,r-1): # 위 방향으로 미세먼지가 이동
        board[i][0]=board[i+1][0]
    
    for i in range(1,c): # 왼쪽 방향으로 미세먼지가 이동
        board[r-1][i-1]=board[r-1][i]
    
    for i in range(r-1,airP,-1): # 아래 방향으로 미세먼지가 이동
        board[i][c-1]=board[i-1][c-1]
    
    for i in range(c-1,1,-1): # 오른쪽 방향으로 미세먼지가 이동
        board[airP][i]=board[airP][i-1]
    board[airP][1]=0 # 공기청정기에서 나오는 공기

for i in range(t):
    dust()
    airPurify()
dust()

board[air[0]][0]=0
board[air[1]][0]=0
totalDust=0
for i in board:
    totalDust+=sum(i)
print(totalDust)