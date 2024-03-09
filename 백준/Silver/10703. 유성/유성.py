import sys
input=sys.stdin.readline

def func():
    r,s=map(int,input().split())
    pic=[]
    x=[]
    xmax=[-r]*s # 가장 낮은 유성 위치
    landmin=[r]*s # 가장 높은 땅 위치
    for i in range(r):
        tmp=list(input().rstrip())
        for j in range(s):
            if tmp[j]=='X':
                x.append([i,j])
                xmax[j]=max(xmax[j],i)
                tmp[j]='.' # 유성을 그림에서 지우기
            elif tmp[j]=='#':
                landmin[j]=min(landmin[j],i)
        pic.append(tmp)
    fall=s # 유성이 떨어지는 거리
    for i in range(s):
        fall=min(fall,landmin[i]-xmax[i]-1)
    
    for i in range(len(x)): # 유성 위치 업데이트
        tx,ty=x[i][0]+fall, x[i][1]
        pic[tx][ty]='X'
        
    for i in range(r):
        print(''.join(pic[i]))
    return

func()